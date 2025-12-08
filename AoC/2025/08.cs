using System;
using System.Numerics;
using System.Reflection;

class AoC08
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        int firstAnswer = 0;
        long secondAnswer = 0;

        List<Vector3> jboxes = [.. File.ReadAllLines(path).Select(r => r.Split(',').Select(x => int.Parse(x)).ToList()).Select(a => new Vector3(a[0], a[1], a[2]))];

        SortedList<float,Stack<Tuple<int,int>>> distances = [];

        for (int i = 0; i < jboxes.Count - 1; i++)
        {
            for (int j = i + 1; j < jboxes.Count; j++)
            {
                float distance = Vector3.Distance(jboxes[i], jboxes[j]);
                if (!distances.TryGetValue(distance, out Stack<Tuple<int, int>>? value))
                {
                    value = [];
                    distances[distance] = value;
                }
                value.Push(new(i,j));
            }
        }

        List<int> circuits = [.. Enumerable.Repeat(-1, jboxes.Count)];
        List<List<int>> circuitsList = [];
        int zeros = circuits.Count;
        int nonZeroesCircuits = 0;

        int k = 0;
        while (true)
        {
            Stack<Tuple<int, int>> stack = distances.Values.First();
            (int i, int j) = stack.Pop();
            if (stack.Count == 0)
            {
                distances.Remove(distances.Keys.First());
            }
            if (circuits[i] == -1)
            {
                if (circuits[j] == -1)
                {
                    circuitsList.Add([i,j]);
                    circuits[i] = circuitsList.Count - 1;
                    circuits[j] = circuitsList.Count - 1;
                    zeros -= 2;
                    nonZeroesCircuits++;
                }
                else
                {
                    circuits[i] = circuits[j];
                    circuitsList[circuits[j]].Add(i);
                    zeros--;
                }
            }
            else
            {
                if (circuits[j] == -1)
                {
                    circuits[j] = circuits[i];
                    circuitsList[circuits[i]].Add(j);
                    zeros--;
                }
                else if (circuits[i] != circuits[j])
                {
                    int toDel = circuits[j];
                    foreach (int ind in circuitsList[toDel])
                    {
                        circuits[ind] = circuits[i];
                        circuitsList[circuits[i]].Add(ind);
                    }
                    circuitsList[toDel] = [];
                    nonZeroesCircuits--;
                }
            }

            if (zeros == 0 && nonZeroesCircuits == 1)
            {
                secondAnswer = (long)jboxes[i].X * (long)jboxes[j].X;
                break;
            }

            k++;
            if (k == 1000)
            {
                int top1 = 0, top2 = 0, top3 = 0;
                foreach (List<int> circuit in circuitsList)
                {
                    int v = circuit.Count;
                    if (v > top1)
                    {
                        top3 = top2;
                        top2 = top1;
                        top1 = v;
                    }
                    else if (v > top2)
                    {
                        top3 = top2;
                        top2 = v;
                    }
                    else if (v > top3)
                    {
                        top3 = v;
                    }
                }
                firstAnswer = top1 * top2 * top3;
            }
        }

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
using System;
using System.Numerics;
using System.Reflection;
using System.Threading.Tasks.Dataflow;

class AoC04
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        int firstAnswer = 0;
        int secondAnswer = 0;

        HashSet<Complex> data = [.. File.ReadAllLines(path).Index().Select(row =>  (row.Index, Item: row.Item.Index().Where(p => p.Item == '@').Select(p => p.Index))).SelectMany(p => p.Item, (a,b) => new Complex(a.Index,b))];

        Complex[] neighbours = [new(-1,-1), new(-1,0), new(-1,1), new(0,-1), new(0,1), new(1,-1), new(1,0), new(1,1)];

        HashSet<Complex> toRemove = [];

        while (true)
        {
            foreach(Complex c in data)
            {
                int cnt = 0;
                foreach (Complex n in neighbours)
                {
                    if (data.Contains(c+n))
                    {
                        cnt++;
                        if (cnt == 4)
                        {
                            break;
                        }
                    }
                }
                if (cnt < 4)
                {
                    toRemove.Add(c);
                }
            }
            if (toRemove.Count == 0)
            {
                break;
            }
            if (secondAnswer == 0)
            {
                firstAnswer = toRemove.Count;
            }
            secondAnswer += toRemove.Count;
            data.ExceptWith(toRemove);
            toRemove = [];
        }

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
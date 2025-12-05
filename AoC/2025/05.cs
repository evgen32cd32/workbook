using System;
using System.Reflection;
using System.Runtime.InteropServices;

class AoC05
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;
        long secondAnswer = 0;

        LinkedList<Tuple<long,long>> ranges = [];
        
        bool firstPart = true;
        foreach (string line in File.ReadAllLines(path))
        {
            if (line == "")
            {
                firstPart = false;
                continue;
            }
            if (firstPart)
            {
                Tuple<long,long> newTuple = (line.Split('-') switch {var v => (long.Parse(v[0]), long.Parse(v[1]))}).ToTuple();
                bool inserted = false;
                if (ranges.First is not null)
                {
                    LinkedListNode<Tuple<long,long>> currentRange = ranges.First;
                
                    while (true)
                    {
                        Tuple<long,long> currentTuple = currentRange.Value;
                        if (newTuple.Item2 < currentTuple.Item1)
                        {
                            ranges.AddBefore(currentRange, newTuple);
                            inserted = true;
                            break;
                        }

                        if (newTuple.Item1 > currentTuple.Item2)
                        {
                            if (currentRange.Next is null)
                            {
                                break;
                            }
                            currentRange = currentRange.Next;
                            continue;
                        }

                        newTuple = new(Math.Min(newTuple.Item1, currentTuple.Item1), Math.Max(newTuple.Item2, currentTuple.Item2));
                        if (currentRange.Next is null)
                        {
                            ranges.Remove(currentRange);
                            break;
                        }
                        LinkedListNode<Tuple<long,long>> toDelete = currentRange;
                        currentRange = currentRange.Next;
                        ranges.Remove(toDelete);
                    }
                }
                if (!inserted)
                {
                    ranges.AddLast(newTuple);
                }
                continue;
            }
            long ingridient = long.Parse(line);
            foreach (Tuple<long,long> pair in ranges)
            {
                if (pair.Item1 <= ingridient && ingridient <= pair.Item2)
                {
                    firstAnswer += 1;
                    break;
                }
            }
        }

        secondAnswer = ranges.Select(p => p.Item2 - p.Item1 + 1).Sum();

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
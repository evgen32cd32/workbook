using System;
using System.ComponentModel;
using System.Reflection;
using System.Runtime.Intrinsics.Arm;

class AoC02
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";
        
        HashSet<long> first = [];
        HashSet<long> second = [];

        foreach (string range in File.ReadAllLines(path)[0].Split(','))
        {
            string[] data = range.Split('-');
            long a = long.Parse(data[0]);
            long b = long.Parse(data[1]);
            long times = 1;
            while (true) // times++
            {
                times += 1;

                bool flag = false;
                long mult = 1;
                while (true) // pattern++
                {
                    mult *= 10;

                    long pattern = 1;
                    long m = mult;
                    for (long i = 1; i < times; i++)
                    {
                        pattern += m;
                        m *= mult;
                    }
                    if (b < pattern)
                    {
                        break;
                    }
                    flag = true;

                    long start, stop;
                    stop = Math.Min(b / pattern, mult - 1);
                    start = a / pattern;
                    if (a % pattern > 0)
                    {
                        start += 1;
                    }
                    start = Math.Max(start, mult / 10);

                    for (long i = start; i <= stop; i++)
                    {
                        second.Add(i * pattern);
                        if (times == 2)
                        {
                            first.Add(i * pattern);
                        }
                    }
                }
                if (!flag)
                {
                    break;
                }
            }
        }

        Console.WriteLine($"First answer: {first.Sum()}");
        Console.WriteLine($"Second answer: {second.Sum()}");
    }
}
using System;
using System.Reflection;

class AoC07
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        int firstAnswer = 0;
        long secondAnswer = 0;

        string[] input = File.ReadAllLines(path);

        Dictionary<int,long> beams = [];

        beams[input[0].IndexOf('S')] = 1;
        
        for (int i = 1; i < input.Length; i++)
        {
            Dictionary<int,long> newBeams = [];
            foreach (KeyValuePair<int,long> pair in beams)
            {
                if (input[i][pair.Key] == '^')
                {
                    newBeams.TryAdd(pair.Key - 1, 0);
                    newBeams[pair.Key - 1] += pair.Value;
                    newBeams.TryAdd(pair.Key + 1, 0);
                    newBeams[pair.Key + 1] += pair.Value;
                    firstAnswer += 1;
                }
                else
                {
                    newBeams.TryAdd(pair.Key, 0);
                    newBeams[pair.Key] += pair.Value;
                }
            }
            beams = newBeams;
        }

        secondAnswer = beams.Values.Sum();

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
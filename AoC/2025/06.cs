using System;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

class AoC06
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;
        long secondAnswer = 0;

        string[] input = File.ReadAllLines(path);

        List<Func<long,long,long>> operations = [.. input[^1].Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(GetFunction)];

        List<long> values = [.. input[0].Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => long.Parse(x))];
        
        for (int i = 1; i <= input.Length - 2; i++)
        {
            List<long> newValues = [.. input[i].Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => long.Parse(x))];
            for (int j = 0; j < values.Count; j++)
            {
                values[j] = operations[j](values[j],newValues[j]);
            }
        }

        firstAnswer = values.Sum();

        Func<long,long,long> foo = GetFunction("+");
        long value = 0;
        for (int j = 0; j < input[0].Length; j++)
        {
            if (input[^1][j] != ' ')
            {
                foo = GetFunction(input[^1][j].ToString());
                value = input[^1][j] == '+' ? 0 : 1;
            }
            string number = "";
            for (int i = 0; i < input.Length - 1; i++)
            {
                number += input[i][j];
            }
            if (long.TryParse(number, out long n))
            {
                value = foo(value, n);
            }
            else
            {
                secondAnswer += value;
            }
        }
        secondAnswer += value;

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");

        Func<long,long,long> GetFunction(string c)
        {
            if (c == "+")
            {
                return  (a, b) => a+b;
            }
            else
            {
                return (a, b) => a*b;
            }
        }
    }
}
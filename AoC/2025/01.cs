using System;
using System.Reflection;

class AoC01
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        int curValue = 50;

        int firstAnswer = 0;
        int secondAnswer = 0;
        
        foreach (string cmd in File.ReadAllLines(path))
        {
            bool flag = curValue == 0;
            curValue += (cmd[0] == 'L' ? -1 : 1) * int.Parse(cmd[1..]);
            secondAnswer += Math.Abs(curValue / 100);
            if (curValue > 0 && curValue % 100 == 0)
                secondAnswer -= 1;
            curValue %= 100;
            if (curValue < 0)
            {
                curValue += 100;
                if (!flag)
                    secondAnswer += 1;
            }
            if (curValue == 0)
                firstAnswer++;
        }

        secondAnswer += firstAnswer;

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
using System.Reflection;

class AoC03
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;
        long secondAnswer = 0;
        
        foreach (string bank in File.ReadAllLines(path))
        {
            int[] intBank = [.. bank.Select(c => int.Parse(c.ToString()))];
            firstAnswer += FindTopJoltage(intBank, 2);
            secondAnswer += FindTopJoltage(intBank, 12);
        }

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }

    private static long FindTopJoltage(int[] bank, int batteryCount)
    {
        int[] top = new int[batteryCount];
        int[] indexes = new int[batteryCount];
        for (int i = 0; i < batteryCount; i++)
        {
            int start = i == 0 ? 0 : indexes[i-1] + 1;
            for (int j = start; j <= bank.Length - batteryCount + i; j++)
            {
                if (top[i] < bank[j])
                {
                    top[i] = bank[j];
                    indexes[i] = j;
                    if (top[i] == 9)
                    {
                        break;
                    }
                }
            }
        }
        long mult = 10;
        long answer = top[^1];
        for (int i = 2; i <= batteryCount; i++)
        {
            answer += top[^i] * mult;
            mult *= 10;
        }
        return answer;
    }
}
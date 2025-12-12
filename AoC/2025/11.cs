using System.Reflection;

class AoC11
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;
        long secondAnswer = 0;

        Dictionary<string,List<string>> devices = [];
        Dictionary<string,long> visits = [];

        foreach (string row in File.ReadAllLines(path))
        {
            string device = row.Split(':')[0];
            devices[device] = [.. row.Split(':')[1].Split()[1..]];
        }
        devices["out"] = [];

        long Recursion(string device, string end, Dictionary<string,long> memory)
        {
            if (memory.TryGetValue(device, out long value))
            {
                return value;
            }
            if (device == end)
            {
                memory[device] = 1;
                return 1;
            }
            if (devices[device].Count == 0)
            {
                memory[device] = 0;
                return 0;
            }
            memory[device] = devices[device].Select(x => Recursion(x, end, memory)).Sum();
            return memory[device];
        }

        firstAnswer = Recursion("you", "out", []);

        long dacToOut = Recursion("dac","out", []);
        long svrToFft = Recursion("svr","fft", []);
        long fftToDac = Recursion("fft","dac", []);

        long dacToFft = Recursion("dac","fft",[]);
        long fftToOut = Recursion("fft","out",[]);
        long svrToDac = Recursion("svr","dac",[]);

        secondAnswer = svrToFft * fftToDac * dacToOut + svrToDac * dacToFft * fftToOut;

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
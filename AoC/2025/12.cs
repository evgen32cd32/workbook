using System.Numerics;
using System.Reflection;

class AoC12
{
    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;

        int bad = 0;
        int unknown = 0;

        bool first = true;
        List<HashSet<Complex>> presents = [];
        int i = 0;

        foreach (string row in File.ReadAllLines(path))
        {
            if (row == "")
            {
                continue;
            }
            if (row[1] != ':' && row[1] != '#' & row[1] != '.')
            {
                first = false;
            }
            if (first)
            {
                if (row[1] == ':')
                {
                    presents.Add([]);
                    i = 0;
                    continue;
                }
                presents[^1].UnionWith([.. row.Index().Where(c => c.Item == '#').Select(c => new Complex(i,c.Index))]);
                i++;
            }
            else
            {
                string[] splitted = row.Split(':');
                List<int> size = [.. splitted[0].Split('x').Select(int.Parse)];
                int totalTiles = size[0] * size[1];
                int spaces3x3 = (size[0] / 3) * (size[1] / 3);
                List<int> prs = [.. splitted[1][1..].Split().Select(int.Parse)];
                if (prs.Sum() <= spaces3x3)
                {
                    firstAnswer++;
                    continue;
                }
                if (prs.Index().Select(x => x.Item * presents[x.Index].Count()).Sum() > totalTiles)
                {
                    bad++;
                    continue;
                }
                unknown++;
            }
        }

        //Console.WriteLine(unknown); //0

        Console.WriteLine($"First answer: {firstAnswer}");
    }
}
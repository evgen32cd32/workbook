using System.Diagnostics;
using System.Reflection;
using System.Runtime.CompilerServices;

class AoC09
{
    struct Pair
    {
        public long X;
        public long Y;

        public Pair(long x, long y)
        {
            X = x;
            Y = y;
        }

        public Pair(string row)
        {
            List<long> list = [.. row.Split(',').Select(long.Parse)];
            X = list[0];
            Y = list[1];
        }

        public readonly override string ToString()
        {
            return $"({X}, {Y})";
        }

        public static Pair operator +(Pair left, Pair right)
        {
            return new(left.X + right.X, left.Y + right.Y);
        }

        public static List<Pair> directions = [
            new(0, 1),
            new(0, -1),
            new(-1, 0),
            new(1, 0)
        ];
    }

    public static void Main(string[] args)
    {
        string declaringTypeName = MethodBase.GetCurrentMethod()?.DeclaringType?.Name ?? "";
        string shortSuffix = declaringTypeName.Length >= 2 ? declaringTypeName[^2..] : declaringTypeName;
        string path = $"../../../../../data/advent2025/advent_{shortSuffix}.txt";

        long firstAnswer = 0;
        long secondAnswer = 0;

        string[] input = File.ReadAllLines(path);

        List<Pair> redTiles = [.. File.ReadAllLines(path).Select(row => new Pair(row))];

        List<long> coordsX = [.. redTiles.Select(v => v.X).ToHashSet()];
        coordsX.Sort();
        List<long> coordsY = [.. redTiles.Select(v => v.Y).ToHashSet()];
        coordsY.Sort();

        Dictionary<long,int> dictX = coordsX.Index().Select(v => (Key: v.Item, Value: v.Index)).ToDictionary();
        Dictionary<long,int> dictY = coordsY.Index().Select(v => (Key: v.Item, Value: v.Index)).ToDictionary();

        HashSet<Pair> border = [];
        Pair prev = new(dictX[redTiles[^1].X], dictY[redTiles[^1].Y]);

        foreach(Pair tile in redTiles)
        {
            Pair newCoords = new(dictX[tile.X], dictY[tile.Y]);
            border.Add(newCoords);
            for (long x = Math.Min(prev.X, newCoords.X) + 1; x < Math.Max(prev.X, newCoords.X); x++)
            {
                border.Add(new(x, newCoords.Y));
            }
            for (long y = Math.Min(prev.Y, newCoords.Y) + 1; y < Math.Max(prev.Y, newCoords.Y); y++)
            {
                border.Add(new(newCoords.X, y));
            }
            prev = newCoords;
        }

        HashSet<Pair> empty = [];
        HashSet<Pair> toVisit = [new(-1, -1)];
        while (toVisit.Count > 0)
        {
            HashSet<Pair> newToVisit = [];
            empty.UnionWith(toVisit);
            foreach (Pair pair in toVisit)
            {
                foreach (Pair d in Pair.directions)
                {
                    Pair newPair = pair + d;
                    if (!empty.Contains(newPair) && !border.Contains(newPair) && newPair.X >= -1 && newPair.Y >= -1 && newPair.X <= coordsX.Count && newPair.Y <= coordsY.Count)
                    {
                        newToVisit.Add(newPair);
                    }
                }
            }
            toVisit = newToVisit;
        }

        /*for (int x = 0; x < coordsX.Count; x++)
        {
            for (int y = 0; y < coordsY.Count; y++)
            {
                Pair pair = new(x, y);
                if (border.Contains(pair))
                {
                    Console.Write('+');
                }
                else if (empty.Contains(pair))
                {
                    Console.Write('.');
                }
                else
                {
                    Console.Write(' ');
                }
            }
            Console.Write('\n');
        }*/

        for (int i = 0; i < redTiles.Count - 1; i++)
        {
            for (int j = i + 1; j < redTiles.Count; j++)
            {
                long square = (Math.Abs(redTiles[i].X - redTiles[j].X) + 1) * (Math.Abs(redTiles[i].Y - redTiles[j].Y) + 1);
                firstAnswer = Math.Max(firstAnswer, square);

                //Console.WriteLine($"{redTiles[i]} {redTiles[j]} {square}");

                if (square <= secondAnswer)
                {
                    continue;
                }

                bool flag = false;
                Pair minTile = new(dictX[Math.Min(redTiles[i].X, redTiles[j].X)], dictY[Math.Min(redTiles[i].Y, redTiles[j].Y)]);
                Pair maxTile = new(dictX[Math.Max(redTiles[i].X, redTiles[j].X)], dictY[Math.Max(redTiles[i].Y, redTiles[j].Y)]);
                for (long x = minTile.X; x <= maxTile.X; x++)
                {
                    if(empty.Contains(new(x, minTile.Y)) || empty.Contains(new(x, maxTile.Y)))
                    {
                        flag = true;
                        break;
                    }
                }
                if (flag)
                {
                    continue;
                }
                for (long y = minTile.Y; y <= maxTile.Y; y++)
                {
                    if(empty.Contains(new(minTile.X, y)) || empty.Contains(new(maxTile.X, y)))
                    {
                        flag = true;
                        break;
                    }
                }
                if (!flag)
                {
                    secondAnswer = square;
                }
            }
        }

        Console.WriteLine($"First answer: {firstAnswer}");
        Console.WriteLine($"Second answer: {secondAnswer}");
    }
}
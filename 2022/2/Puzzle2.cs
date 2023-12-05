using adventofcode;

namespace AdventOfCode22.Day02
{
    public class Puzzle2
    {
        public const string INPUTFILE = "inputtest";
        public static void Run()
        {
            string[] lines = File.ReadAllLines(Program.GetInputPath(INPUTFILE, "Day02"));
            int totalScore = 0;
            foreach (string line in lines)
            {
                char opponent = line[0];
                char player = line[2];
                totalScore += ObjToScore(player, opponent) + GameScore(player);
            }
            Console.WriteLine(totalScore);
        }

        private static int GameScore(char player)
        {
            return player switch
            {
                'X' => 0,
                'Y' => 3,
                _ => 6
            };
        }

        private static int ObjToScore(char player, char opponent)
        {
            return player switch
            {
                'X' => opponent switch
                {
                    'A' => 3,
                    'B' => 1,
                    _ => 2,
                },
                'Y' => opponent switch
                {
                    'A' => 1,
                    'B' => 2,
                    _ => 3,
                },
                _ => opponent switch
                {
                    'A' => 2,
                    'B' => 3,
                    _ => 1,
                },
            };
        }
    }
}

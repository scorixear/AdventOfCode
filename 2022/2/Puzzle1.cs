using adventofcode;

namespace AdventOfCode22.Day02
{
    public class Puzzle1
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
                totalScore += ObjToScore(player) + GameScore(player, opponent);
            }
            Console.WriteLine(totalScore);
        }

        private static int GameScore(char playerNotation, char opponentNotation)
        {
            char player = NotationToObj(playerNotation);
            char opponent = NotationToObj(opponentNotation);
            if (player == opponent)
                return 3;
            if (player == 'R')
            {
                if (opponent == 'P')
                    return 0;
            }
            else if (player == 'P')
            {
                if (opponent == 'S')
                    return 0;
            }
            else
            {
                if (opponent == 'R')
                    return 0;
            }
            return 6;
        }

        private static int ObjToScore(char notation)
        {
            char obj = NotationToObj(notation);
            return obj switch
            {
                'R' => 1,
                'P' => 2,
                _ => 3,
            };
        }

        private static char NotationToObj(char notation)
        {
            if (notation == 'A' || notation == 'X')
                return 'R';
            if (notation == 'B' || notation == 'Y')
                return 'P';
            return 'S';
        }
    }
}

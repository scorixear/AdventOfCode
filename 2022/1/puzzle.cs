using System;

namespace adventofcode {
  public class Day01 {
    private const string INPUTFILE = "input";
    public static void Run() {
      string[] input = File.ReadAllLines(Program.GetInputPath(INPUTFILE, "Day01"));
      int[] maxCalories = new int[]{0,0,0};
      int currentCalories = 0;
      foreach(string rawLine in input) {
        string line = rawLine.Trim();
        if (string.IsNullOrEmpty(line)) {
          if (maxCalories[0] < currentCalories) {
            maxCalories[0] = currentCalories;
            maxCalories = maxCalories.Order().ToArray();
          }
          currentCalories = 0;
        } else {
          currentCalories += int.Parse(line);
        }
      }
      if (maxCalories[0] < currentCalories) {
        maxCalories[0] = currentCalories;
        maxCalories = maxCalories.Order().ToArray();
      }
      Console.WriteLine($"{maxCalories.Sum()}");
    }
  }
}
use std::fs;
use std::env;
use std::path::Path;

pub fn solve() {
  let path = env::current_dir().unwrap().join("/src/01/input");
  println!("{:?}", path);
  let data = fs::read_to_string(&path).expect( &format!("File not found: {:?}", path));
  let lines = data.split('\n');

  let mut max_calories = [0,0,0];
  let mut current_calories = 0;
  for line in lines {
    if line == "" {
      if max_calories[0] < current_calories {
        max_calories[0] = current_calories;
        max_calories.sort()
      }
      current_calories = 0;
    } else {
      current_calories += line.parse::<i32>().expect("Invalid Input");
    }
  }
  if max_calories[0] < current_calories {
    max_calories[0] = current_calories;
  }
  let sum: i32 = max_calories.iter().sum();
  println!("{}", sum)
}
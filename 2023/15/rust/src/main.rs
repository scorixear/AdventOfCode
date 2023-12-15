use std::time::Instant;
pub struct HashMap {
    table: [Vec<(String, usize)>; 256]
}

impl HashMap {
    pub fn new() -> HashMap {
        HashMap {
            table: core::array::from_fn(|_| Vec::new())
        }
    }

    pub fn add_or_set(&mut self, key: String, value: usize) {
        let hash = self.hash(&key);
        let bucket = &mut self.table[hash as usize];
        for (i, (k, _)) in bucket.iter().enumerate() {
            if k == &key {
                bucket[i] = (key, value);
                return;
            }
        }
        bucket.push((key, value));
    }

    pub fn remove(&mut self, key: String) {
        let hash = self.hash(&key);
        let bucket = &mut self.table[hash as usize];
        for (i, (k, _)) in bucket.iter().enumerate() {
            if k == &key {
                bucket.remove(i);
                return;
            }
        }
    }

    pub fn get_focus_power(&self) -> usize {
        let mut power = 0;
        for (i, bucket) in self.table.iter().enumerate() {
            for (j, (_, v)) in bucket.iter().enumerate() {
                power += (i+1)*(j+1)*v;
            }
        }
        power
    }

    fn hash(&self, key: &String) -> u32 {
        let mut curr: u32 = 0;
        for c in key.chars() {
            curr += c as u32;
            curr *= 17;
            curr %= 256;
        }
        curr
    }
}


fn run() {
    let text = std::fs::read_to_string("input.txt").expect("Could not find file").trim().to_string();
    let sequences = text.split(",").map(|s| s.to_string()).collect::<Vec<String>>();

    let mut map = HashMap::new();
    for s in sequences {
        if s.ends_with("-") {
            map.remove(s.trim_end_matches("-").to_string());
        } else {
            let mut vals = s.split("=");
            let key = vals.next().expect("No key found").to_string();
            let str_value = vals.next().expect("No value found");
            let value = match str_value.parse::<usize>() {
                Ok(v) => v,
                Err(_) => panic!("Could not parse value {str_value}", str_value=str_value)
            };
            map.add_or_set(key, value)
        }
    }
    println!("Focus power: {}", map.get_focus_power());
}

fn main() {

    let before = Instant::now();
    run();
    println!("Time: {}ms", (before.elapsed().as_nanos() as f64)/1000000.0)
    
}

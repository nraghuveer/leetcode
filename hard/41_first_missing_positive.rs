impl Solution {
    pub fn first_missing_positive(nums_original: Vec<i32>) -> i32 {
        // take a copy
        let mut nums = nums_original.clone();
        let N = nums.len() as i32;
        for (index, num) in nums_original.iter().enumerate() {
            if num < &1 || num > &N {
                nums[index] = N+1;
            }
        }
        // mark the index as visited by making the value negative
        for index in 0..nums.len() {
            let mut value = nums[index].abs() as usize;
            if value > N as usize {
                continue;
            }
            value = value - 1;
            if nums[value] > 0 {
                nums[value] = -1 * nums[value] as i32;
            }
        }
        println!("{:?}", nums);
        // get the first index, wich is having positive value
        for index in 0..nums.len() {
            if nums[index] > 0 {
                return index as i32 + 1;
            }
        }
        N+1
    }
}

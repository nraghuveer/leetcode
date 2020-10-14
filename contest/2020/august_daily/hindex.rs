impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        // index in the vector is the number or name of the publication by author
        // the value gives the number of times it has been published.
        // calc h, the array has h elements having value atleast h
        // this means, the h <= N
        let ans = vec![0; citations.len()];
        for citiation in citations.iter() {

        }
    }
}
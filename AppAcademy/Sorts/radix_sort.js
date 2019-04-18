function radixSort(arr) {
    if(!Array.isArray(arr)) return null;
    if(arr.length === 1) return arr;
    const buckets = new Array(10).fill(null).map(() => new Array(0));
    const times = getMaxDigits(arr);
    let buffer = arr.slice(0);
    const ret = [];
    for(let i = 0; i < times + 1; i++){
        buffer.forEach(num => { 
            if(getLength(num) >= i + 1)
                buckets[getDigit(num, i)].push(num);
            else
                ret.push(num);
        });
        buffer = [];
        for(let i = 0; i < buckets.length; i++){
            buffer = buffer.concat(buckets[i]);
            buckets[i] = [];
        }
    }
    return ret;
}

const getDigit = (num, place) => Math.floor(Math.abs(num) / 10 ** place) % 10;
const getLength = num => num === 0 ? 1 : Math.floor(Math.log10(Math.abs(num))) + 1;
const getMaxDigits = nums => {
    let max = 0;
    for(let i = 0; i < nums.length; i++){
        max = Math.max(max, getLength(nums[i]));
    }
    return max;
};


module.exports = {
    radixSort
};
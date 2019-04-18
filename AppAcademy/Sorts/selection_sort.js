function swap(arr, index1, index2) {
    const temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
}

function selectionSort(arr){
    let start = 0;
    while(start < arr.length - 1){
        let smallest = start;
        for(let i = start; i < arr.length; i++){
            if(arr[i] < arr[smallest]) smallest = i;  
        }
        swap(arr, smallest, start);
        start++;
    }
    return arr;
}

module.exports = {
    selectionSort,
    swap
};
function merge(array1, array2) {
    const ret = [];
    while(array1.length > 0 && array2.length > 0){
        if(array1[0] > array2[0])
            ret.push(array2.shift());
        else
            ret.push(array1.shift());
    }
    return ret.concat(array1, array2);
}

function mergeSort(array) {
    if(array.length <= 1) return array;
    const mid = Math.floor(array.length / 2);
    return merge(mergeSort(array.slice(0, mid)), mergeSort(array.slice(mid)));
}

module.exports = {
    merge,
    mergeSort
};
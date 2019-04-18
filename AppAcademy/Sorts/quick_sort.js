function quickSort(array) {
    if(array.length <= 1) return array;
    const pivot = array[0];
    return quickSort(array.slice(1).filter(el => el < pivot)).concat([pivot],  quickSort(array.slice(1).filter(el => el >= pivot)));
}


module.exports = {
    quickSort
};
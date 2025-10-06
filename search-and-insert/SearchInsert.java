public class SearchInsert {
  public static void main(String[] args) {
    int[] arr = {1,2,3,4,5};
    int result = search(arr, 6);
    System.out.println(result);
  }

  //solution
  public static int search(int[] arr, int target){
    int low = 0;
    int high = arr.length - 1;
    while (low <= high){
      int mid =(int) Math.floor((low + high) / 2);
      if (target == arr[mid]){
        return mid;
      }else if (target > arr[mid]){
        low = mid + 1;
      }else{
        high = mid - 1;
      }
    }
    return low;
  }
}

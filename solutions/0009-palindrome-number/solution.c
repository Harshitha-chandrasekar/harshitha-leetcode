bool isPalindrome(int x) {
    int copy = x;
    long rev =0;
    while(copy>0){
        rev = rev*10 + copy%10;
        copy = copy/10;
    }
    if(rev == (long)x)
        return true;
    else
        return false;
}

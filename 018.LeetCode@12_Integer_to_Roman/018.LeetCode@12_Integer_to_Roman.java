class Solution {
    public String intToRoman(int num) {
        StringBuilder str = new StringBuilder();
        int temp = num ;
        while(temp>=1000){
            str.append('M');
            temp-=1000;
        }
        while(temp>=900){
            str.append("CM");
            temp-=900;
        }
        while(temp>=500){
            str.append('D');
            temp-=500;
        }
        while(temp>=400){
            str.append("CD");
            temp-=400;
        }
        while(temp>=100){
            str.append('C');
            temp-=100;
        }
        while(temp>=90){
            str.append("XC");
            temp-=90;
        }
        while(temp>=50){
            str.append('L');
            temp-=50;
        }
        while(temp>=40){
            str.append("XL");
            temp-=40;
        }
        while(temp>=10){
            str.append('X');
            temp-=10;
        }
        while(temp>=9){
            str.append("IX");
            temp-=9;
        }
        while(temp>=5){
            str.append('V');
            temp-=5;
        }
        while(temp>=4){
            str.append("IV");
            temp-=4;
        }
        while(temp>=1){
            str.append('I');
            temp-=1;
        }

        return str.toString() ;
    }
}
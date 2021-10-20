let a;
let i;
a=prompt('Ededi daxil edin: ')
while(a!=0){
    i=a%10
    if (i%2==1) {
      console.log(i);
    }
    a=Math.floor(a/10)
    

}
alert(i)
//proqram yalniz en sondaki tek ededi cap etdi

function Nov(a){
    return (typeof(a));
}
function kvadrat(a){
    return (a*a);
}
function metn(a){
    return "bu bir metndir";
}

let a= prompt('deyeri daxil edin: ')
a=Number(a)
if (typeof(a)=='string'){
    let netice= metn(a)
    let netice2=Nov(a)
    console.log(netice,netice2)

}
    else if (typeof(a)=='number'){
        
    let netice=kvadrat(a)
    console.log(netice)
    }
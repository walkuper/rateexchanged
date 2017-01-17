$(function(){
function slipt_str(array){
                    var r = [];
                    for(var i = 0, l = array.length; i < l; i++) {
                        for(var j = i + 1; j < l; j++)
                            if (array[i] === array[j]) j = ++i;
                            r.push(array[i]);
                    }
                    return r;
}
function slipt_str2(array){
                    array.sort; 
                    var re=[array[0]];
                    for(var i = 1; i < array.length; i++){
                        if( array[i] !== re[re.length-1])
                        {
                            re.push(array[i]);
                        }
                    }
                    return re;
}
})
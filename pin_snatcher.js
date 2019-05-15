document.createElement = function(create) {
    return function() {
        var ret = create.apply(this, arguments);
        ret.setAttribute = function(setattribute){
        	return function(){
        		if (arguments[1].includes("pinimg")){
        			console.log(arguments[1])
        		}
        	}
        }(ret.setattribute)
        return ret;
    };
}(document.createElement)
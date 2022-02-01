function submitEntry() {
	var inputtext = document.getElementById('inputText');
	var loginLoader = document.getElementById('loginLoader');
	var submitbtn = document.getElementById('submitbtn');

	submitbtn.style.display = 'none';
	loginLoader.style.display = 'block'

	var entry = {
		'text':inputtext.value
	}

	 fetch(`${window.origin}/sent_correct`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(entry),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json"
                })
            })
            .then(function (response){
                if (response.status !== 200){
                    console.log("Response Status was not 200");
                    return ;
                }

                response.json().then(function (data) {

                    if (data.error == 'no-error'){
                        document.getElementById('outputText').value = data.text
                        submitbtn.style.display = 'block';
						loginLoader.style.display = 'none'
                    }else{
                    	document.getElementById('outputText').value = data.error
                        submitbtn.style.display = 'block';
						loginLoader.style.display = 'none'
                }

                })
            })
}
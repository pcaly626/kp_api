
 const  get_singapore_one_data = async () =>{

    let response = await fetch('http://localhost:8000/pop/1',{method:"GET",headers:{'Content-Type':'application/json'}})
    const data = response.json()
    return data;
}


get_singapore_one_data().then( data => {
    document.querySelector('#district').append(data.name)
    document.querySelector('#population').append(data.population)
})
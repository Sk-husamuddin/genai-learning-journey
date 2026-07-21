async function getmsg(){
    const response = await fetch("https://dummyjson.com/products/1");

    const data = await response.json();
    console.log(data.title);
}

getmsg();
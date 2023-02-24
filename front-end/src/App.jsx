import React, {useState, useEffect} from 'react';

function App () {
    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/names")
            .then(res => res.json())
            .then(data => {
                setData(data)
                console.log(data);
            })
    },[])

    return <>
        {
            (typeof data.names === "undefined") ? ( <p>Loading...</p> )
            :
            (data.names.map((name) => (
                <p key={name} > {name} </p>
            )))
        }
    </>
}

export default App
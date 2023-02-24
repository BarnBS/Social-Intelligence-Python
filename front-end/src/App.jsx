// import React, {useState, useEffect} from 'react';
import { useQuery } from 'react-query';

async function fetchNames() {
    const res = await fetch("/names");
    return res.json();
};

function App () {
    const {isLoading, data, isError} = useQuery("names",fetchNames)
    
    if (isError) {
        return <div> Error </div>
    }
    
    if (isLoading) {
        return <div> Loading ... </div>
    }


    return <>
        {
            data.names.map((name) => (
                <p key={name} > {name} </p>
            ))
        }
    </>
}

export default App
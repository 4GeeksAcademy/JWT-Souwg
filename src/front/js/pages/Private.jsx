import { useEffect } from "react";
import React from "react";
import { useNavigate } from "react-router-dom";

const Private = () =>{

    const navigate = useNavigate()

useEffect(() =>{
    if (!window.sessionStorage.getItem('token')){
        return navigate('/login')
    }
},[])
    return <div className="container-fluid text-center">
        <h1>If you are seeing this</h1>
        <p>It's probably because you have an item called token in your session Storage or simply because you're logged in... Who Knows?</p> </div>
}

export default Private
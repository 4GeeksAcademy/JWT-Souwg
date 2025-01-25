import React, {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

const SessionForm = ({register = true}) =>{
const navigate = useNavigate()
const [emailValue, setEmailValue] = useState("")
const [passwordValue, setPasswordValue] = useState("")


    const handleSubmit = async (e) => {
        e.preventDefault()
       const email = emailValue.trim()
       const password = passwordValue.trim()
        if (!register){
        let res = await fetch("https://verbose-space-cod-jj4gv9j44676c59qj-3001.app.github.dev/api/login",{
            headers:{
                "Content-Type": "application/json"
            },
            method: "POST",
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        })
        if(res.status == 200){
            let data = await res.json()
            sessionStorage.setItem("token",data.token)
            console.log("Inicio de sesion Exitoso")
            navigate("/private")
        }else{
            alert("Credenciales invalidas")
        }
        }else{
        let res = await fetch("https://verbose-space-cod-jj4gv9j44676c59qj-3001.app.github.dev/api/signup",{
            headers:{
                "Content-Type": "application/json"
            },
            method: "POST",
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        })
        if (res.ok){
            let data = await res.json()
            console.log(data)
            navigate("/login")
        }else{
            console.error("Error creating user")
            return
        }
    }

    setEmailValue("")
    setPasswordValue("")

    }

    useEffect(() =>{
        if (window.sessionStorage.getItem('token')){
            navigate("/private")
        }
    },[])


    return <div className="container-fluid d-flex flex-column align-items-center">
        <h1>{register ? "Registro" : "Iniciar Sesion"}</h1>
    <form onSubmit={(e) => handleSubmit(e)}>
        <div className="form-group mb-2">
            <label htmlFor="emailInput">Email</label>
            <input type="email" name="emailInput" className="form-control" value={emailValue} onChange={(e)=> setEmailValue(e.target.value)}/>
        </div>
        <div className="form-group mb-2">
            <label htmlFor="emailInput">Password</label>
            <input type="password" name="passwordInput" className="form-control" value={passwordValue} onChange={(e) => setPasswordValue(e.target.value)}/>
        </div>
        <div className="d-flex gap-4 justify-content-center">

        <button className="btn btn-primary ">{register ? "Registrarse": "Iniciar sesion"}</button>
        {register ? (<Link to={"/login"} className="btn btn-success">Login</Link>):""}
        </div>
    </form>
    </div>
    
}

export default SessionForm
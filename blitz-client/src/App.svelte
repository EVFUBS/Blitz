<script lang="ts">
import { Router, Route, Link } from "svelte-navigator";
import Nav from "./components/Navigation/Navbar.svelte";
import About from "./pages/About.svelte";
import Explore from "./pages/Explore.svelte";
import Home from "./pages/Home.svelte";
import Play from "./pages/play.svelte";
import SignIn from "./pages/SignIn.svelte";
import SignUp from "./pages/SignUp.svelte";
import Create from "./pages/Create.svelte";
import Questions from "./components/Create/Questions.svelte";
import Settings from "./pages/Settings.svelte";
import { csrf, themeColor, themeColor2, themeColorAlt } from "./store"
import Account from "./pages/Account.svelte";
const getCSRF = async() => {
  const response = await fetch("/api/auth/csrf/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  });
  const data = await response.json();
  csrf.set(data.csrf_token);
  console.log($csrf);
};


getCSRF();

document.documentElement.style.setProperty('--theme-color', $themeColor)
document.documentElement.style.setProperty('--theme-color-2', $themeColor2)
document.documentElement.style.setProperty('--theme-color-alt', $themeColorAlt)

</script>

<Router>
  <Nav />
  <main>
    <Route path='/'>
      <Home/>
    </Route>
  
    <Route path='/about'>
      <About/>
    </Route>
  
    <Route path='/play'>
      <Play/>
    </Route>
  
    <Route path='/explore'>
      <Explore/>
    </Route>
  
    <Route path='/create'>
      <Create/>
    </Route>

    <Route path='/signin'>
      <SignIn/>
    </Route>
  
    <Route path='/signup'>
      <SignUp/>
    </Route>

    <Route path='/account'>
      <Account/>
    </Route>

    <Route path='/settings'>
      <Settings/>
    </Route>
  </main>
</Router>

<style>
  :global(body){
    margin: 0;
    padding: 0;
    font-family: monospace;
  }

  :global(.blueButton){
    color: #0070f3;
    border: #0070f3 solid 2px;
    border-radius: 5px;
    text-decoration: none;
    font-family: monospace;
    font-size: 0.9rem;
    font-weight: bold;
    transition: 0.2s;
    background-color: white;
    box-sizing: border-box;
  }

  :global(.blueButton:hover){
    background-color: #0070f3;
    color: white;
  }

  :global(.redButton){
    color: #e3200a;
    border: #e3200a solid 2px;
    border-radius: 5px;
    text-decoration: none;
    font-family: monospace;
    font-size: 0.9rem;
    font-weight: bold;
    transition: 0.2s;
    background-color: white;
    box-sizing: border-box;
  }

  :global(.redButton:hover){
    background-color: #e3200a;
    color: white;
  }

  main{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }


</style>

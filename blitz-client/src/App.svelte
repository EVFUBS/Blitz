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


import { csrf } from "./store"
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
  </main>
</Router>

<style>
  :global(body){
    margin: 0;
    padding: 0;
    font-family: monospace;
  }
</style>

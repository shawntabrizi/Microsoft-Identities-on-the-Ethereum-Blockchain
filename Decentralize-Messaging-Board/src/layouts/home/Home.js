import React, { Component } from 'react'
import { AccountData, ContractData, ContractForm } from 'drizzle-react-components'
import logo from '../../logo.png'
import PropTypes from 'prop-types'


var totalPosts = 0;
class Home extends Component {

  constructor(props, context) {
    super(props)
    this.contracts = context.drizzle.contracts;
    console.log(this.contracts["DMB"].methods);
    this.dataKey = this.contracts["DMB"].methods["erc721TokenId"].cacheCall();
    this.state = {
      login: false,
      tenantId: "", 
      loginId: ""
    };
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  createPostTable = () => {
    let table = []

    // Outer loop to create parent
    for (let i = 1; i < totalPosts; i++) {
      //Create the parent and add the children
      table.push(
        <div style={{"backgroundColor":"lightblue"}}>
        <h2>Author Affiliation: </h2>
        <ContractData contract="DMB" method="getPostAuthorAffiliation" methodArgs={[i]}/>
        <h2>Author TenantId: </h2>
        <ContractData contract="DMB" method="getTokenTenantId" methodArgs={[i]}/>
        <h2>Author Address: </h2>
        <ContractData contract="DMB" method="ownerOf" methodArgs={[i]}/>
        <h2>Content: </h2>
        <p>
        <ContractData contract="DMB" method="tokenURI" methodArgs={[i]}/>
        </p>
        <br/><br/>
        </div>
      );
    }
    return table
  }
  handleSubmit() {
    this.state.tenantId = this.state.loginId;
  }

  handleInputChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }
  render() {
    var self = this;
    // if(this.state.tenantId > 0){
      
    // }
    this.contracts.DMB.methods.login().call().then(function(pass){
      if(!pass){
        self.state.login= false;
      }else{
        self.state.login = true;
      }
    });
    if(!self.state.login){
      return (
            <main className="container">
              <div className="container">
                <p>Youre wallet address is not authenticated. Please go to <a href="https://shawntabrizi.com/msidoneth/">link</a> to register</p>
              </div>
            </main>
      );
    }
    // if(!this.state.login || !this.state.tenantId){
    //   var message = null;

    //   if(this.state.tenantId > 0){
    //     message = <p>Wrong credential/tenantId</p>;
    //   }else{
    //     message = <p>You're no log in please log in with the proper tenantId</p>
    //   }
    //   return (
    //     <main className="container">
    //       <div className="container">
    //         {message}
    //         <form className="pure-form pure-form-stacked">
    //         <input key="loginId" name="loginId" value={this.state["loginId"]} placeholder="tenantId" onChange={this.handleInputChange} />
    //           <button key="submit" className="pure-button" type="button" onClick={this.handleSubmit}>Login</button>
    //         </form>
    //       </div>
    //       <div className="container">
    //         <p>Register a new tenantId</p>
    //         <div className="pure-u-1-1">
    //         <h2>Decentralize Messaging Board Registration</h2>
    //         <p>Hack way to create tenantId</p>
    //         <ContractForm contract="DMB" method="setTenantId" />
    //         <br/><br/>
    //       </div>
    //       </div>
    //     </main>
    //   );
    //}
    //Get total number of the posts
    // var displayData = 0;
    // if(!this.contracts.DMB.initialized) {
    //   displayData = -1;

    // } else 
    // // If the cache key we received earlier isn't in the store yet; the initial value is still being fetched.
    // if(!(this.dataKey in this.contracts.DMB["erc721TokenId"])) {
    //   displayData = -2;

    // }else{ 
    //   displayData = this.contracts.DMB.erc721TokenId[this.dataKey].value
    // }

    // console.log(displayData);
    this.contracts.DMB.methods.erc721TokenId().call().then(function(num){
        totalPosts = num;
    });
  
    return (
      <main className="container">
        <div className="pure-g">
          <div className="pure-u-1-1 header">
            <img src={logo} alt="drizzle-logo" />
            <h1>Drizzle Examples</h1>
            <p>Examples of how to get started with Drizzle in various situations.</p>

            <br/><br/>
          </div>
        
          <div className="pure-u-1-1">
            <h2>Active Account</h2>
            <AccountData accountIndex="0" units="ether" precision="3" />
            <br/><br/>
          </div>
          <div className="pure-u-1-1">
            <p>Register a new tenantId</p>
            <h2>Decentralize Messaging Board Registration</h2>
            <p>Hack way to create tenantId</p>
            <ContractForm contract="DMB" method="setTenantId" />
            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>Decentralize Messaging Board Demo</h2>
            <p>Simple way to post a new post</p>
            <ContractForm contract="DMB" method="createNewPost" />
            <br/><br/>
          </div>
          <div className="pure-u-1-1">
            {
              this.createPostTable()
            }
            <br/><br/>
          </div>
        </div>
    </main>
    );
  }
}

Home.contextTypes = {
  drizzle: PropTypes.object
}

export default Home

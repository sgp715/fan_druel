import React from "react";

import teamsStore from "../stores/Team.js";
import fileStore from "../stores/File.js";

import * as teamActions from "../actions/TeamActions.js";
import * as fileActions from "../actions/FileActions.js";

export default class Page extends React.Component {

    constructor() {
        super();
        this.state = {
                       team: teamsStore.getAll(),
                       file: fileStore.getAll(),
                     };
    }

    componentWillMount() {

        teamsStore.on("change", () => {
            this.setState({team: teamsStore.getAll()});
        })

        fileStore.on("change", () => {
            this.setState({file: fileStore.getAll()})
        })
    }

    getTeam() {

        var rows = [];

        if (this.state.team) {
            var i;
            for (i = 0; i < this.state.team.length; i++) {
                rows.push(<tr key={this.state.team[i]} ><td>{this.state.team[i]}</td></tr>);
            }
        } else {
            rows = <tr key="placeholder"><td> Team not yet generated</td></tr>;
        }

        return rows;
    }

    // toggleAlert() {
    //     // console.log("toggle");
    //     this.setState({alert: !this.alert});
    // }

    // shouldAlert(){
    //
    //     // console.log("shouldAlert");
    //     // console.log(this.state.alert);
    //
    //     if (this.state.alert) {
    //         return (
    //             <div class="alert alert-dismissible alert-danger">
    //                 <button type="button" onClick={this.toggleAlert.bind(this)} class="close" data-dismiss="alert">&times;</button>
    //                 <strong>Oh snap!</strong> Try uploading a file first knuckle head.
    //             </div>
    //         )
    //     }
    // }


    handleClick(){

        if (this.state.file) {

            console.log("New file calculating team");

            //d
            var reader = new FileReader();

            reader.onload = (event) => {

                var data = event.target.result;
                // console.log(data);
                // TODO: get the from env
                var teamEndpoint = window.location + 'bestTeam';
                console.log("Sending to " + teamEndpoint);
                fetch(teamEndpoint, {
                  method: 'POST',
                  headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ file: data })
                })
                .then((response) => response.json())
                .then((responseJson) => {
                    // console.log(responseJson.team);
                    teamActions.createTeam(responseJson.team);
                })

            };
            reader.onerror =  (e) => {
                console.log("Could not read exited with error : " + e);
            };

            var data = reader.readAsText(this.state.file);

            fileActions.updateFile(null);
        } else {
            console.log("Not a new file");
        }

    }

    handleFile(){

        var x = document.getElementById("csvFile");

        var numberFiles = x.files.length;

        if (numberFiles == 1){

            console.log("File updating");

            var file = x.files[0];
            fileActions.updateFile(file);
            console.log(file);
        } else if (numberFiles > 1) {
            console.log("Only taking one file at time");
        }

    }

    render(){
        return (
            <div class="container-fluid">
                <nav class="navbar navbar-default">
                    <div class="navbar-brand">FanDruel</div>
                </nav>
                <div class="panel">
                    <h3>Choose CSV file for FanDuel competition: </h3>
                        <input type="file" onChange={this.handleFile.bind(this)} id="csvFile" />
                    <h3>Generate Team</h3>
                    <input type="button" class="btn btn-primary" onClick={this.handleClick.bind(this)} value="Go!" id="generate"/>
                </div>
                <h3>Best possible team to choose: </h3>
                <table class="table">
                    <tbody>
                        {this.getTeam()}
                    </tbody>
                </table>
            </div>
        );
    }

}

import React from "react";

import generateStore from "../stores/Generate.js";
import teamsStore from "../stores/Teams.js";

import * as generateActions from "../actions/GenerateActions.js";

export default class Page extends React.Component {

    constructor() {
        super();
        this.state = {
                       generate: generateStore.getAll(),
                       team: teamsStore.getAll()
                     };
    }

    componentWillMount() {
        generateStore.on("change", () => {
            this.setState({generate: generateStore.getAll()});
        });
    }

    getTeam() {

        var rows = [];

        if (this.state.generate) {
            var i;
            for (i = 0; i < this.state.team.length; i++) {
                rows.push(<tr key={this.state.team[i]} ><td>{this.state.team[i]}</td></tr>);
            }
        } else {
            rows = <tr key="placeholder"><td> Team not yet generated</td></tr>;
        }

        return rows;
    }

    handleClick(){
        generateActions.toggleGenerate();
    }

    // shouldAlert(){
    //
    //     if (this.state.generate) {
    //         return (
    //             <div class="alert alert-dismissible alert-danger">
    //                 <button type="button" class="close" data-dismiss="alert">&times;</button>
    //                 <strong>Oh snap!</strong> <a href="#" class="alert-link">Change a few things up</a> and try submitting again.
    //             </div>
    //         )
    //     }
    //
    // }

    render(){
        return (
            <div class="container-fluid">
                <div class="jumbotron">
                    <h1> FanDruel </h1>
                    <p> FanDruel takes in a CSV file for an NBA competition and uses machine learning
                    to pick the best team for your fantasy competition.</p>
                </div>
                <div class="well">
                    <h2>Choose CSV file for FanDuel competition: </h2>
                        <input type="file" id="csvFile" />
                    <h2>Generate Team</h2>
                    <input type="button" class="btn btn-primary" onClick={this.handleClick.bind(this)} value="Go!" id="generate"/>
                </div>
                <h2>Best possible team to choose: </h2>
                <table class="table">
                    <tbody>
                        {this.getTeam()}
                    </tbody>
                </table>
            </div>
        );
    }

}

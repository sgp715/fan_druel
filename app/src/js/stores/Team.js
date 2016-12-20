import { EventEmitter } from "events";

import dispatcher from "../dispatcher.js";

import localStorage from "localStorage";

class TeamStore extends EventEmitter {

    constructor() {
        super();
        this.store = JSON.parse(localStorage.getItem('team')) || null;
    }

    getAll() {

        if (this.store == null) {
            return null;
        }

        return this.store.team;
    }

    createTeam(team) {

        this.store = {team: team};
        this.emit("change");
        this.store = localStorage.setItem('team', JSON.stringify(this.store));


    }

    handleAction(action) {
        switch(action.type) {
            case "CREATE_TEAM": {
                console.log("Action");
                console.log(action.team);
                this.createTeam(action.team);
            }
        }
    }

}

const teamStore = new TeamStore;

dispatcher.register(teamStore.handleAction.bind(teamStore));

export default teamStore;

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

    createTeam() {

        this.store = {team: ["Steph Curry",
                      "Anthony Davis",
                      "Kanye West",
                      "Darius Ruckers",
                      "Bill Nye",
                      "Max Perez",
                      "Carmelo Anthony",
                      "Anthony Montemayor",
                      "Jim George"] };
        this.emit("change");
        this.store = localStorage.setItem('team', JSON.stringify(this.store));


    }

    handleAction(action) {
        switch(action.type) {
            case "CREATE_TEAM": {
                this.createTeam();
            }
        }
    }

}

const teamStore = new TeamStore;

dispatcher.register(teamStore.handleAction.bind(teamStore));

export default teamStore;

import { EventEmitter } from "events";

class TeamsStore extends EventEmitter {

    constructor() {
        super();
        this.teams = ["Me", "You", "Jeff", "Ben", "Mike", "Max", "Rochester", "Claire", "Jim"];
    }

    getAll() {
        return this.teams;
    }

}

const teamsStore = new TeamsStore;

export default teamsStore;

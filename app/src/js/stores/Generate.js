import { EventEmitter } from "events";

import dispatcher from "../dispatcher.js";

import localStorage from "localStorage";

class GenerateStore extends EventEmitter {

    constructor() {
        super();
        this.generate = localStorage.getItem('generate') || false;
    }

    toggleGenerate() {

        if (!this.generate) {
            this.generate = true;
            localStorage.setItem('generate', this.generate);
            this.emit("change");
        }
    }

    getAll() {
        return this.generate;
    }

    handleAction(action) {
        switch(action.type) {
            case "TOGGLE_GENERATE": {
                this.toggleGenerate();
            }
        }
    }

}

const generateStore = new GenerateStore;

dispatcher.register(generateStore.handleAction.bind(generateStore));

export default generateStore;

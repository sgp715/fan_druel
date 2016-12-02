var casper = require('casper').create();

// switch it over to FanDuel :O
login_url = 'https://www.fanduel.com/p/login#login';

casper.start(login_url, function() {
    this.echo('NAVIGATING TO LOGIN');
    this.echo(this.getTitle());
    this.echo('\n');
});

var creds = require('./creds.json');
casper.then(function() {

    var inputemail = 'input#email';
    if (this.exists(inputemail)) {
        this.echo('SENDING EMAIL\n');
        this.sendKeys(inputemail, creds.email);
    } else {
        this.echo('Could not find place for email - exiting').exit();
    }

    var inputPassword = 'input#password';
    if (this.exists(inputPassword)) {
        this.echo('SENDING PASSWORD\n');
        this.sendKeys(inputPassword, creds.password);
    } else {
        this.echo('Could not find place for password - exiting').exit();
    }

});

casper.then(function(){
    this.capture('Login.png');
});


casper.then(function() {

    var loginButton = 'input.login-card-button';
    if (this.exists(loginButton)) {
        this.echo('CLICKING LOGIN\n');
        this.click(loginButton);
    } else {
        this.echo('Could not find login button - exiting').exit();
    }

});

casper.then(function(){
    this.capture('Loggedin.png');
});

casper.run();

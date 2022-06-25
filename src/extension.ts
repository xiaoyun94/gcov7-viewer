// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "gcov7-viewer" is now active!');

	let gcovAdapter: string = context.asAbsolutePath("gcov7-json.py");
	vscode.workspace.getConfiguration().update("gcovViewer.gcovBinary", gcovAdapter, vscode.ConfigurationTarget.Global);
	vscode.window.showInformationMessage('[gcovViewer.gcovBinary] has been replaced with gcov7-json adapter');

}

// this method is called when your extension is deactivated
export function deactivate() {
	vscode.workspace.getConfiguration().update("gcovViewer.gcovBinary", null, vscode.ConfigurationTarget.Global);
}

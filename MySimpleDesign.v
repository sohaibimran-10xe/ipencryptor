`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/05/2024 10:55:28 AM
// Design Name: 
// Module Name: MySimpleDesign
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module MySimpleDesign(
    input wire a,  // First input (mapped to FPGA pin)
    input wire b,  // Second input (mapped to FPGA pin)
    output wire y  // Output (mapped to FPGA pin)
    );
    
    // XOR logic
    assign y = a ^ b;
endmodule

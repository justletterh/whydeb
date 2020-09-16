@echo off
gcc o1.c -o o1.exe
go build w.go
rustc d.rs
.\bin\bf !3.bf !3.exe
javac credit.java
# Cycle Pricing Engine

## Overview

The Cycle Pricing Engine is designed to replace manual Excel-based
cycle pricing.

A cycle contains multiple components such as frames, gear sets,
tyres and brakes. Component prices can change over time, so the
system maintains price history and selects the valid price based
on the effective date.

## Problem

The sales team currently manages cycle pricing manually using Excel.
This can cause errors when component prices change.

For example:

- Tyre price in January: ₹200
- Tyre price in December: ₹230

The system should automatically use the correct price based on the
selected date.

## Solution

The system contains:

- Component management
- Component price history
- Effective date-based pricing
- Cycle configuration
- Automatic total price calculation
- Admin price management

## Main Design

### Class Model

- Component
- ComponentPrice
- PricingService

### Pricing Flow

User selects components
        ↓
Pricing Service
        ↓
Find valid price
        ↓
Apply quantity
        ↓
Calculate total
        ↓
Return final cycle price

## Example

Frame = ₹5,000  
Gear Set = ₹2,000  
Tyre × 2 = ₹460  
Brake = ₹800

Total = ₹8,260

## Technology

- Python
- Object-Oriented Programming
- Date-based price validation

## How to Run

```bash
python cycle_pricing.py

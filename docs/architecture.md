# GuardX Proposed Architecture

## Initial Concept

GuardX is planned as a multi-stage image privacy analysis and protection
system.

The initial workflow is:

```text
              IMAGE
                |
                v
        +----------------+
        | Image Analysis |
        +-------+--------+
                |
        +-------+-------+
        |               |
        v               v
 Visible Information   Hidden Information
        |               |
        v               v
   Text / Objects       EXIF
   Documents            GPS
   QR / Barcode         Timestamp
        |               |
        +-------+-------+
                |
                v
        Privacy Analysis
                |
                v
       User Recommendations
                |
                v
        Privacy Protection
                |
                v
        Sanitized Image
                |
                v
           Verification
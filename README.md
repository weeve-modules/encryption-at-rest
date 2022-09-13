# Encryption At Rest

|              |                                                            |
| ------------ | ---------------------------------------------------------- |
| name         | Encryption At Rest                                         |
| version      | v1.0.0                                                     |
| GitHub       | [encryption-at-rest](https://github.com/weeve-modules/encryption-at-rest) |
| DockerHub    | [weevenetwork/encryption-at-rest](https://hub.docker.com/r/weevenetwork/encryption-at-rest)     |
| authors      | Paul Gaiduk                                                |

***
## Table of Content

- [Encryption At Rest](#encryption-at-rest)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Module Variables](#module-variables)
  - [Module Testing](#module-testing)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

This module extrapolates and enctypts the data it receives, while also forwarding the received JSON to the next module. It also calculates the entropy of the encrypted data and the plaintext and logs both.

## Module Variables

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| INPUT_LABEL           | string | The input label on which anomaly is detected |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)    |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received               |
| INGRESS_PORT          | string | Port to which data will be received               |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module            |

## Module Testing

TBD

## Dependencies

The following are module dependencies:

* bottle
* requests
* cryptography
* numpy
* scipy

The following are developer dependencies:

* pytest
* flake8
* black

## Input

Input to this module is JSON body single object:

Example of single object:

```json
{
  temperature: 15
}
```


## Output
Output of this module is JSON body the same as input data:

```json
{
  temperature: 15
}
```

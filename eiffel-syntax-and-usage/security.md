<!---
   Copyright 2017-2018 Ericsson AB.
   For a full list of individual contributors, please see the commit history.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
--->

# Security
Let us begin by establishing that the Eiffel protocol by itself can be considered neither _secure_ nor _insecure_, any more than English is secure or French is insecure. Security is not a property of the language or the protocol as such, but of how it is communicated and managed. That being said, security is a highly relevant concern, and where feasible Eiffel supports it. It is important to understand that security is a broad concept, however, and that feasibility varies depending on the type of security in question. In literature, the three key concepts of security (sometimes referred to as the CIA triad) are confidentiality, integrity and availability. We will discuss each of these in turn.

## Confidentiality
In the words of ISO27000, confidentiality means that "information is not made available or disclosed to unauthorized individuals, entities, or processes". This can be achieved through multiple (and often complementary) means, such as encryption and access control. The Eiffel protocol itself cannot support confidentiality; instead it is a property of the systems used to transport, process and store the Eiffel events. In other words, if the confidentiality of information communicated as Eiffel events is a concern for you, then you are recommended to take appropriate action to ensure the confidentiality of your data, both at rest and in transit, e.g. through encryption.

## Integrity
In information security, integrity refers to the accuracy and completeness of data. In other words, safeguarding integrity requires protection against both malicious and unintentional tampering with or corruption of data in an unauthorized or undetected manner. This cannot be _solved_ by a communication protocol, as it relies on adequate infrastructure and processes for managing the data, but it can be _supported_. Eiffel supports data integrity through digital signatures.

A digital signature is a combination of hashing technology and encryption. Hash functions are commonly used to ensure data integrity and are familiar to most software professionals. By using checksums or hash values (particularly hash values, or _digests_, produced by cryptographic hash functions such as the SHA series), any piece of data of arbitrary length is computed into a fixed length digest, with any alteration of the input data resulting in a different digest. Consequently, as long as the digest of the received data matches the digest of the data sent, its integrity can be verified. Unfortunately, the digest must be securely communicated: any malicious attacker able to not only manipulate the data but also the digest can make a corrupted message appear authentic. This is why digital signing also employs encryption.

The Eiffel protocol's support is influenced by [JSON Web Signatures (JWS)](https://tools.ietf.org/html/rfc7515), with slight modifications to allow inclusion of the signature within the event message itself, rather than as part of a header. This serves to keep every Eiffel event self-contained, with information integrity protection optional for the producer to include and optional for the consumer to consider. Note that this optionality does not in any way lessen the strength of the security provided: it is always up to the recipient of an unprotected Eiffel event to decide whether to trust it or not. In this sense, Eiffel support of data integrity is very similar to that employed by other document formats, such as the [Portable Document Format](http://www.adobe.com/devnet/pdf/pdf_reference.html).

## Availability
Availability of information communicated over the Eiffel protocol is a property of the communication channels and storage solutions used. In other words, similarly to confidentiality, it is an infrastructural concern and external to the protocol itself.

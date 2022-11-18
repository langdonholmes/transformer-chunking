# Research Notes

Case study of "got to" ("need to") versus "got to" ("was allowed to") embeddings in a pre-trained transformer model.
"got to" can have several meanings. We are interested in the sense that is roughly the same as "need to" as opposed to the sense of "was allowed to." In my speech, "got to" meaning "need to" typically has an alternate pronunciation of "gotta," whereas "got to" meaning "was allowed to" is pronounced as two separate words, "got" and "to".

This type of phonological alternation has been used to argue that "got to" meaning "need to" is a singular, freestanding lexical item, despite that our writing systems suggests two words, "got" and "to".

The hypothesis is that a transformer model will learn to chunk information about the construction "got to," as humans are expected to do. We will test this by looking at the degree to which the embeddings for the construction vary as compared to embedding variance in the alternative meaning "was allowed to."

## Procedure:
Extract embeddings for "got" and "to" in different natural sentences. Measure variance to test hypothesis.

### Data:
Example sentences containing "got to" and "went to" will be sampled from COCA and verfied by hand to ensure consistency in the sense of the constructions.

### Measurement:
The last hidden state for the relevant tokens will be sampled from each example sentence.

### Analysis:



Possible Outcomes:

1. "to" has a similar range of locations in the vector space whether it is part of "got to" or part of another construction. --> This would suggest that "got" and "to" are processed analytically, and this method would find no evidence of chunking.  
This should be tested with a similar verb held constant for which there is no phonological evidence of chunking. "went to" might be a reasonable candidate here.
2. "to" has significantly more variance in the vector space when it is part of the construction "got to." --> This would suggest that the semantics of "got to" are chunked and stored in the token "got," and "to" contains more information about its context and less information about itself.
3. "to" has significantly less variance in the vector space when it is part of the construction "got to." --> This would suggest that "to" is functioning as the headword for the construction, carrying most of its semantic content and capturing relatively little information about its context.
4. The outcomes can be interpreted similarly for "got," but certain combinations of outcomes for "got" and "to" might require a more developed analysis.

# Do Over

Let's use an analysis that is based on information retention.

Do more word-y words retain more token-specific information through the layers of the transformer blocks? Do compositional words like "got to" retain less token-specific information as they move through the transformer blocks?

Does the predictability of a token affect how much of its initial token embed is retained?
"""GraphQL-core

The primary :mod:`graphql` package includes everything you need to define a GraphQL
schema and fulfill GraphQL requests.

GraphQL-core provides a reference implementation for the GraphQL specification
but is also a useful utility for operating on GraphQL files and building sophisticated
tools.

This top-level package exports a general purpose function for fulfilling all steps
of the GraphQL specification in a single operation, but also includes utilities
for every part of the GraphQL specification:

  - Parsing the GraphQL language.
  - Building a GraphQL type schema.
  - Validating a GraphQL request against a type schema.
  - Executing a GraphQL request against a type schema.

This also includes utility functions for operating on GraphQL types and GraphQL
documents to facilitate building tools.

You may also import from each sub-package directly. For example, the following two
import statements are equivalent::

    from graphql import parse
    from graphql.language import parse

The sub-packages of GraphQL-core 3 are:

  - :mod:`graphql.language`: Parse and operate on the GraphQL language.
  - :mod:`graphql.type`: Define GraphQL types and schema.
  - :mod:`graphql.validation`: The Validation phase of fulfilling a GraphQL result.
  - :mod:`graphql.execution`: The Execution phase of fulfilling a GraphQL request.
  - :mod:`graphql.error`: Creating and formatting GraphQL errors.
  - :mod:`graphql.utilities`:
    Common useful computations upon the GraphQL language and type objects.
"""

# The GraphQL-core 3 and GraphQL.js version info.

from .version import version, version_info, version_js, version_info_js

# Utilities for compatibility with the Python language.
from .pyutils import Undefined, UndefinedType

# Create, format, and print GraphQL errors.
from .error import (
    GraphQLError,
    GraphQLErrorExtensions,
    GraphQLFormattedError,
    GraphQLSyntaxError,
    located_error,
)

# Parse and operate on GraphQL language source files.
from .language import (
    Source,
    get_location,
    # Print source location
    print_location,
    print_source_location,
    # Lex
    Lexer,
    TokenKind,
    # Parse
    parse,
    parse_value,
    parse_const_value,
    parse_type,
    # Print
    print_ast,
    # Visit
    visit,
    ParallelVisitor,
    Visitor,
    VisitorAction,
    VisitorKeyMap,
    BREAK,
    SKIP,
    REMOVE,
    IDLE,
    DirectiveLocation,
    # Predicates
    is_definition_node,
    is_executable_definition_node,
    is_nullability_assertion_node,
    is_selection_node,
    is_value_node,
    is_const_value_node,
    is_type_node,
    is_type_system_definition_node,
    is_type_definition_node,
    is_type_system_extension_node,
    is_type_extension_node,
    # Types
    SourceLocation,
    Location,
    Token,
    # AST nodes
    Node,
    # Each kind of AST node
    NameNode,
    DocumentNode,
    DefinitionNode,
    ExecutableDefinitionNode,
    OperationDefinitionNode,
    OperationType,
    VariableDefinitionNode,
    VariableNode,
    SelectionSetNode,
    SelectionNode,
    FieldNode,
    ArgumentNode,
    NullabilityAssertionNode,
    NonNullAssertionNode,
    ErrorBoundaryNode,
    ListNullabilityOperatorNode,
    ConstArgumentNode,
    FragmentSpreadNode,
    InlineFragmentNode,
    FragmentDefinitionNode,
    ValueNode,
    ConstValueNode,
    IntValueNode,
    FloatValueNode,
    StringValueNode,
    BooleanValueNode,
    NullValueNode,
    EnumValueNode,
    ListValueNode,
    ConstListValueNode,
    ObjectValueNode,
    ConstObjectValueNode,
    ObjectFieldNode,
    ConstObjectFieldNode,
    DirectiveNode,
    ConstDirectiveNode,
    TypeNode,
    NamedTypeNode,
    ListTypeNode,
    NonNullTypeNode,
    TypeSystemDefinitionNode,
    SchemaDefinitionNode,
    OperationTypeDefinitionNode,
    TypeDefinitionNode,
    ScalarTypeDefinitionNode,
    ObjectTypeDefinitionNode,
    FieldDefinitionNode,
    InputValueDefinitionNode,
    InterfaceTypeDefinitionNode,
    UnionTypeDefinitionNode,
    EnumTypeDefinitionNode,
    EnumValueDefinitionNode,
    InputObjectTypeDefinitionNode,
    DirectiveDefinitionNode,
    TypeSystemExtensionNode,
    SchemaExtensionNode,
    TypeExtensionNode,
    ScalarTypeExtensionNode,
    ObjectTypeExtensionNode,
    InterfaceTypeExtensionNode,
    UnionTypeExtensionNode,
    EnumTypeExtensionNode,
    InputObjectTypeExtensionNode,
)

# Utilities for operating on GraphQL type schema and parsed sources.
from .utilities import (
    # Produce the GraphQL query recommended for a full schema introspection.
    # Accepts optional IntrospectionOptions.
    get_introspection_query,
    IntrospectionQuery,
    # Get the target Operation from a Document.
    get_operation_ast,
    # Convert a GraphQLSchema to an IntrospectionQuery.
    introspection_from_schema,
    # Build a GraphQLSchema from an introspection result.
    build_client_schema,
    # Build a GraphQLSchema from a parsed GraphQL Schema language AST.
    build_ast_schema,
    # Build a GraphQLSchema from a GraphQL schema language document.
    build_schema,
    # Extend an existing GraphQLSchema from a parsed GraphQL Schema language AST.
    extend_schema,
    # Sort a GraphQLSchema.
    lexicographic_sort_schema,
    # Print a GraphQLSchema to GraphQL Schema language.
    print_schema,
    # Print a GraphQLType to GraphQL Schema language.
    print_type,
    # Prints the built-in introspection schema in the Schema Language format.
    print_introspection_schema,
    # Create a GraphQLType from a GraphQL language AST.
    type_from_ast,
    # Convert a language AST to a dictionary.
    ast_to_dict,
    # Create a Python value from a GraphQL language AST with a Type.
    value_from_ast,
    # Create a Python value from a GraphQL language AST without a Type.
    value_from_ast_untyped,
    # Create a GraphQL language AST from a Python value.
    ast_from_value,
    # A helper to use within recursive-descent visitors which need to be aware of the
    # GraphQL type system.
    TypeInfo,
    TypeInfoVisitor,
    # Coerce a Python value to a GraphQL type, or produce errors.
    coerce_input_value,
    # Concatenates multiple ASTs together.
    concat_ast,
    # Separate an AST into an AST per Operation.
    separate_operations,
    # Strip characters that are not significant to the validity or execution
    # of a GraphQL document.
    strip_ignored_characters,
    # Comparators for types
    is_equal_type,
    is_type_sub_type_of,
    do_types_overlap,
    # Compare two GraphQLSchemas and detect breaking changes.
    BreakingChange,
    BreakingChangeType,
    DangerousChange,
    DangerousChangeType,
    find_breaking_changes,
    find_dangerous_changes,
)

# Create and operate on GraphQL type definitions and schema.
from .type import (
    # Definitions
    GraphQLSchema,
    GraphQLDirective,
    GraphQLScalarType,
    GraphQLObjectType,
    GraphQLInterfaceType,
    GraphQLUnionType,
    GraphQLEnumType,
    GraphQLInputObjectType,
    GraphQLList,
    GraphQLNonNull,
    # Standard GraphQL Scalars
    specified_scalar_types,
    GraphQLInt,
    GraphQLFloat,
    GraphQLString,
    GraphQLBoolean,
    GraphQLID,
    # Int boundaries constants
    GRAPHQL_MAX_INT,
    GRAPHQL_MIN_INT,
    # Built-in Directives defined by the Spec
    specified_directives,
    GraphQLIncludeDirective,
    GraphQLSkipDirective,
    GraphQLDeferDirective,
    GraphQLStreamDirective,
    GraphQLDeprecatedDirective,
    GraphQLSpecifiedByDirective,
    # "Enum" of Type Kinds
    TypeKind,
    # Constant Deprecation Reason
    DEFAULT_DEPRECATION_REASON,
    # GraphQL Types for introspection.
    introspection_types,
    # Meta-field definitions.
    SchemaMetaFieldDef,
    TypeMetaFieldDef,
    TypeNameMetaFieldDef,
    # Predicates
    is_schema,
    is_directive,
    is_type,
    is_scalar_type,
    is_object_type,
    is_interface_type,
    is_union_type,
    is_enum_type,
    is_input_object_type,
    is_list_type,
    is_non_null_type,
    is_input_type,
    is_output_type,
    is_leaf_type,
    is_composite_type,
    is_abstract_type,
    is_wrapping_type,
    is_nullable_type,
    is_named_type,
    is_required_argument,
    is_required_input_field,
    is_specified_scalar_type,
    is_introspection_type,
    is_specified_directive,
    # Assertions
    assert_schema,
    assert_directive,
    assert_type,
    assert_scalar_type,
    assert_object_type,
    assert_interface_type,
    assert_union_type,
    assert_enum_type,
    assert_input_object_type,
    assert_list_type,
    assert_non_null_type,
    assert_input_type,
    assert_output_type,
    assert_leaf_type,
    assert_composite_type,
    assert_abstract_type,
    assert_wrapping_type,
    assert_nullable_type,
    assert_named_type,
    # Un-modifiers
    get_nullable_type,
    get_named_type,
    # Thunk handling
    resolve_thunk,
    # Validate GraphQL schema.
    validate_schema,
    assert_valid_schema,
    # Uphold the spec rules about naming
    assert_name,
    assert_enum_value_name,
    # Types
    GraphQLType,
    GraphQLInputType,
    GraphQLOutputType,
    GraphQLLeafType,
    GraphQLCompositeType,
    GraphQLAbstractType,
    GraphQLWrappingType,
    GraphQLNullableType,
    GraphQLNullableInputType,
    GraphQLNullableOutputType,
    GraphQLNamedType,
    GraphQLNamedInputType,
    GraphQLNamedOutputType,
    Thunk,
    ThunkCollection,
    ThunkMapping,
    GraphQLArgument,
    GraphQLArgumentMap,
    GraphQLEnumValue,
    GraphQLEnumValueMap,
    GraphQLField,
    GraphQLFieldMap,
    GraphQLFieldResolver,
    GraphQLInputField,
    GraphQLInputFieldMap,
    GraphQLInputFieldOutType,
    GraphQLScalarSerializer,
    GraphQLScalarValueParser,
    GraphQLScalarLiteralParser,
    GraphQLIsTypeOfFn,
    GraphQLResolveInfo,
    ResponsePath,
    GraphQLTypeResolver,
    # Keyword args
    GraphQLArgumentKwargs,
    GraphQLDirectiveKwargs,
    GraphQLEnumTypeKwargs,
    GraphQLEnumValueKwargs,
    GraphQLFieldKwargs,
    GraphQLInputFieldKwargs,
    GraphQLInputObjectTypeKwargs,
    GraphQLInterfaceTypeKwargs,
    GraphQLNamedTypeKwargs,
    GraphQLObjectTypeKwargs,
    GraphQLScalarTypeKwargs,
    GraphQLSchemaKwargs,
    GraphQLUnionTypeKwargs,
)

# Validate GraphQL queries.
from .validation import (
    validate,
    ValidationContext,
    ValidationRule,
    ASTValidationRule,
    SDLValidationRule,
    # All validation rules in the GraphQL Specification.
    specified_rules,
    # Individual validation rules.
    ExecutableDefinitionsRule,
    FieldsOnCorrectTypeRule,
    FragmentsOnCompositeTypesRule,
    KnownArgumentNamesRule,
    KnownDirectivesRule,
    KnownFragmentNamesRule,
    KnownTypeNamesRule,
    LoneAnonymousOperationRule,
    NoFragmentCyclesRule,
    NoUndefinedVariablesRule,
    NoUnusedFragmentsRule,
    NoUnusedVariablesRule,
    OverlappingFieldsCanBeMergedRule,
    PossibleFragmentSpreadsRule,
    ProvidedRequiredArgumentsRule,
    ScalarLeafsRule,
    SingleFieldSubscriptionsRule,
    UniqueArgumentNamesRule,
    UniqueDirectivesPerLocationRule,
    UniqueFragmentNamesRule,
    UniqueInputFieldNamesRule,
    UniqueOperationNamesRule,
    UniqueVariableNamesRule,
    ValuesOfCorrectTypeRule,
    VariablesAreInputTypesRule,
    VariablesInAllowedPositionRule,
    # SDL-specific validation rules
    LoneSchemaDefinitionRule,
    UniqueOperationTypesRule,
    UniqueTypeNamesRule,
    UniqueEnumValueNamesRule,
    UniqueFieldDefinitionNamesRule,
    UniqueArgumentDefinitionNamesRule,
    UniqueDirectiveNamesRule,
    PossibleTypeExtensionsRule,
    # Custom validation rules
    NoDeprecatedCustomRule,
    NoSchemaIntrospectionCustomRule,
)

# Execute GraphQL documents.
from .execution import (
    execute,
    execute_sync,
    default_field_resolver,
    default_type_resolver,
    get_argument_values,
    get_directive_values,
    get_variable_values,
    # Types
    ExecutionContext,
    ExecutionResult,
    ExperimentalIncrementalExecutionResults,
    InitialIncrementalExecutionResult,
    SubsequentIncrementalExecutionResult,
    IncrementalDeferResult,
    IncrementalStreamResult,
    IncrementalResult,
    FormattedExecutionResult,
    FormattedInitialIncrementalExecutionResult,
    FormattedSubsequentIncrementalExecutionResult,
    FormattedIncrementalDeferResult,
    FormattedIncrementalStreamResult,
    FormattedIncrementalResult,
    # Subscription
    subscribe,
    create_source_event_stream,
    MapAsyncIterable,
    # Middleware
    Middleware,
    MiddlewareManager,
)

# The primary entry point into fulfilling a GraphQL request.
from .graphql import graphql, graphql_sync

INVALID = Undefined  # deprecated alias

# The GraphQL-core version info.
__version__ = version
__version_info__ = version_info

# The GraphQL.js version info.
__version_js__ = version_js
__version_info_js__ = version_info_js


__all__ = [
    "version",
    "version_info",
    "version_js",
    "version_info_js",
    "graphql",
    "graphql_sync",
    "GraphQLSchema",
    "GraphQLDirective",
    "GraphQLScalarType",
    "GraphQLObjectType",
    "GraphQLInterfaceType",
    "GraphQLUnionType",
    "GraphQLEnumType",
    "GraphQLInputObjectType",
    "GraphQLList",
    "GraphQLNonNull",
    "specified_scalar_types",
    "GraphQLInt",
    "GraphQLFloat",
    "GraphQLString",
    "GraphQLBoolean",
    "GraphQLID",
    "GRAPHQL_MAX_INT",
    "GRAPHQL_MIN_INT",
    "specified_directives",
    "GraphQLIncludeDirective",
    "GraphQLSkipDirective",
    "GraphQLDeferDirective",
    "GraphQLStreamDirective",
    "GraphQLDeprecatedDirective",
    "GraphQLSpecifiedByDirective",
    "TypeKind",
    "DEFAULT_DEPRECATION_REASON",
    "introspection_types",
    "SchemaMetaFieldDef",
    "TypeMetaFieldDef",
    "TypeNameMetaFieldDef",
    "is_schema",
    "is_directive",
    "is_type",
    "is_scalar_type",
    "is_object_type",
    "is_interface_type",
    "is_union_type",
    "is_enum_type",
    "is_input_object_type",
    "is_list_type",
    "is_non_null_type",
    "is_input_type",
    "is_output_type",
    "is_leaf_type",
    "is_composite_type",
    "is_abstract_type",
    "is_wrapping_type",
    "is_nullable_type",
    "is_named_type",
    "is_required_argument",
    "is_required_input_field",
    "is_specified_scalar_type",
    "is_introspection_type",
    "is_specified_directive",
    "assert_schema",
    "assert_directive",
    "assert_type",
    "assert_scalar_type",
    "assert_object_type",
    "assert_interface_type",
    "assert_union_type",
    "assert_enum_type",
    "assert_input_object_type",
    "assert_list_type",
    "assert_non_null_type",
    "assert_input_type",
    "assert_output_type",
    "assert_leaf_type",
    "assert_composite_type",
    "assert_abstract_type",
    "assert_wrapping_type",
    "assert_nullable_type",
    "assert_named_type",
    "get_nullable_type",
    "get_named_type",
    "resolve_thunk",
    "validate_schema",
    "assert_valid_schema",
    "assert_name",
    "assert_enum_value_name",
    "GraphQLType",
    "GraphQLInputType",
    "GraphQLOutputType",
    "GraphQLLeafType",
    "GraphQLCompositeType",
    "GraphQLAbstractType",
    "GraphQLWrappingType",
    "GraphQLNullableType",
    "GraphQLNullableInputType",
    "GraphQLNullableOutputType",
    "GraphQLNamedType",
    "GraphQLNamedInputType",
    "GraphQLNamedOutputType",
    "Thunk",
    "ThunkCollection",
    "ThunkMapping",
    "GraphQLArgument",
    "GraphQLArgumentMap",
    "GraphQLEnumValue",
    "GraphQLEnumValueMap",
    "GraphQLField",
    "GraphQLFieldMap",
    "GraphQLFieldResolver",
    "GraphQLInputField",
    "GraphQLInputFieldMap",
    "GraphQLInputFieldOutType",
    "GraphQLScalarSerializer",
    "GraphQLScalarValueParser",
    "GraphQLScalarLiteralParser",
    "GraphQLIsTypeOfFn",
    "GraphQLResolveInfo",
    "ResponsePath",
    "GraphQLTypeResolver",
    "GraphQLArgumentKwargs",
    "GraphQLDirectiveKwargs",
    "GraphQLEnumTypeKwargs",
    "GraphQLEnumValueKwargs",
    "GraphQLFieldKwargs",
    "GraphQLInputFieldKwargs",
    "GraphQLInputObjectTypeKwargs",
    "GraphQLInterfaceTypeKwargs",
    "GraphQLNamedTypeKwargs",
    "GraphQLObjectTypeKwargs",
    "GraphQLScalarTypeKwargs",
    "GraphQLSchemaKwargs",
    "GraphQLUnionTypeKwargs",
    "Source",
    "get_location",
    "print_location",
    "print_source_location",
    "Lexer",
    "TokenKind",
    "parse",
    "parse_value",
    "parse_const_value",
    "parse_type",
    "print_ast",
    "visit",
    "ParallelVisitor",
    "TypeInfoVisitor",
    "Visitor",
    "VisitorAction",
    "VisitorKeyMap",
    "BREAK",
    "SKIP",
    "REMOVE",
    "IDLE",
    "DirectiveLocation",
    "is_definition_node",
    "is_executable_definition_node",
    "is_nullability_assertion_node",
    "is_selection_node",
    "is_value_node",
    "is_const_value_node",
    "is_type_node",
    "is_type_system_definition_node",
    "is_type_definition_node",
    "is_type_system_extension_node",
    "is_type_extension_node",
    "SourceLocation",
    "Location",
    "Token",
    "Node",
    "NameNode",
    "DocumentNode",
    "DefinitionNode",
    "ExecutableDefinitionNode",
    "OperationDefinitionNode",
    "OperationType",
    "VariableDefinitionNode",
    "VariableNode",
    "SelectionSetNode",
    "SelectionNode",
    "FieldNode",
    "ArgumentNode",
    "NullabilityAssertionNode",
    "NonNullAssertionNode",
    "ErrorBoundaryNode",
    "ListNullabilityOperatorNode",
    "ConstArgumentNode",
    "FragmentSpreadNode",
    "InlineFragmentNode",
    "FragmentDefinitionNode",
    "ValueNode",
    "ConstValueNode",
    "IntValueNode",
    "FloatValueNode",
    "StringValueNode",
    "BooleanValueNode",
    "NullValueNode",
    "EnumValueNode",
    "ListValueNode",
    "ConstListValueNode",
    "ObjectValueNode",
    "ConstObjectValueNode",
    "ObjectFieldNode",
    "ConstObjectFieldNode",
    "DirectiveNode",
    "ConstDirectiveNode",
    "TypeNode",
    "NamedTypeNode",
    "ListTypeNode",
    "NonNullTypeNode",
    "TypeSystemDefinitionNode",
    "SchemaDefinitionNode",
    "OperationTypeDefinitionNode",
    "TypeDefinitionNode",
    "ScalarTypeDefinitionNode",
    "ObjectTypeDefinitionNode",
    "FieldDefinitionNode",
    "InputValueDefinitionNode",
    "InterfaceTypeDefinitionNode",
    "UnionTypeDefinitionNode",
    "EnumTypeDefinitionNode",
    "EnumValueDefinitionNode",
    "InputObjectTypeDefinitionNode",
    "DirectiveDefinitionNode",
    "TypeSystemExtensionNode",
    "SchemaExtensionNode",
    "TypeExtensionNode",
    "ScalarTypeExtensionNode",
    "ObjectTypeExtensionNode",
    "InterfaceTypeExtensionNode",
    "UnionTypeExtensionNode",
    "EnumTypeExtensionNode",
    "InputObjectTypeExtensionNode",
    "execute",
    "execute_sync",
    "default_field_resolver",
    "default_type_resolver",
    "get_argument_values",
    "get_directive_values",
    "get_variable_values",
    "ExecutionContext",
    "ExecutionResult",
    "ExperimentalIncrementalExecutionResults",
    "InitialIncrementalExecutionResult",
    "SubsequentIncrementalExecutionResult",
    "IncrementalDeferResult",
    "IncrementalStreamResult",
    "IncrementalResult",
    "FormattedExecutionResult",
    "FormattedInitialIncrementalExecutionResult",
    "FormattedSubsequentIncrementalExecutionResult",
    "FormattedIncrementalDeferResult",
    "FormattedIncrementalStreamResult",
    "FormattedIncrementalResult",
    "Middleware",
    "MiddlewareManager",
    "subscribe",
    "create_source_event_stream",
    "MapAsyncIterable",
    "validate",
    "ValidationContext",
    "ValidationRule",
    "ASTValidationRule",
    "SDLValidationRule",
    "specified_rules",
    "ExecutableDefinitionsRule",
    "FieldsOnCorrectTypeRule",
    "FragmentsOnCompositeTypesRule",
    "KnownArgumentNamesRule",
    "KnownDirectivesRule",
    "KnownFragmentNamesRule",
    "KnownTypeNamesRule",
    "LoneAnonymousOperationRule",
    "NoFragmentCyclesRule",
    "NoUndefinedVariablesRule",
    "NoUnusedFragmentsRule",
    "NoUnusedVariablesRule",
    "OverlappingFieldsCanBeMergedRule",
    "PossibleFragmentSpreadsRule",
    "ProvidedRequiredArgumentsRule",
    "ScalarLeafsRule",
    "SingleFieldSubscriptionsRule",
    "UniqueArgumentNamesRule",
    "UniqueDirectivesPerLocationRule",
    "UniqueFragmentNamesRule",
    "UniqueInputFieldNamesRule",
    "UniqueOperationNamesRule",
    "UniqueVariableNamesRule",
    "ValuesOfCorrectTypeRule",
    "VariablesAreInputTypesRule",
    "VariablesInAllowedPositionRule",
    "LoneSchemaDefinitionRule",
    "UniqueOperationTypesRule",
    "UniqueTypeNamesRule",
    "UniqueEnumValueNamesRule",
    "UniqueFieldDefinitionNamesRule",
    "UniqueArgumentDefinitionNamesRule",
    "UniqueDirectiveNamesRule",
    "PossibleTypeExtensionsRule",
    "NoDeprecatedCustomRule",
    "NoSchemaIntrospectionCustomRule",
    "GraphQLError",
    "GraphQLErrorExtensions",
    "GraphQLFormattedError",
    "GraphQLSyntaxError",
    "located_error",
    "get_introspection_query",
    "IntrospectionQuery",
    "get_operation_ast",
    "introspection_from_schema",
    "build_client_schema",
    "build_ast_schema",
    "build_schema",
    "extend_schema",
    "lexicographic_sort_schema",
    "print_schema",
    "print_type",
    "print_introspection_schema",
    "type_from_ast",
    "value_from_ast",
    "value_from_ast_untyped",
    "ast_from_value",
    "ast_to_dict",
    "TypeInfo",
    "coerce_input_value",
    "concat_ast",
    "separate_operations",
    "strip_ignored_characters",
    "is_equal_type",
    "is_type_sub_type_of",
    "do_types_overlap",
    "find_breaking_changes",
    "find_dangerous_changes",
    "BreakingChange",
    "BreakingChangeType",
    "DangerousChange",
    "DangerousChangeType",
    "Undefined",
    "UndefinedType",
]

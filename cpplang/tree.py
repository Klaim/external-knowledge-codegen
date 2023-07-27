
from .ast import Node

# ------------------------------------------------------------------------------


class TranslationUnit(Node):
    attrs = ()


class Import(Node):
    attrs = ("path", "static", "wildcard")


class OverrideAttr(Node):
    attrs = ()


class Documented(Node):
    attrs = ("documentation",)


class Comment(Node):
    attrs = ("comment",)


class FullComment(Comment):
    attrs = ()


class BlockCommandComment(Comment):
    attrs = ()


class ParagraphComment(Comment):
    attrs = ()


class TextComment(Comment):
    attrs = ()


class Declaration(Documented):
    attrs = ()


class EmptyDeclaration(Declaration):
    attrs = ()


class NonEmptyDeclaration(Declaration):
    attrs = ("modifiers", "annotations")


class TypeDeclaration(NonEmptyDeclaration):
    attrs = ("name",)

    @property
    def fields(self):
        return [decl for decl in self.body if isinstance(decl,
                                                         FieldDecl)]

    @property
    def methods(self):
        return [decl for decl in self.body if isinstance(decl,
                                                         MethodDecl)]

    @property
    def constructors(self):
        return [decl for decl in self.body if isinstance(
          decl, ConstructorDeclaration)]


class PackageDeclaration(NonEmptyDeclaration):
    attrs = ("name",)


class CXXRecordDecl(TypeDeclaration):
    attrs = ("kind", "bases", "complete_definition",)


class CXXConstructorDecl(Node):
    attrs = ("name", "noexcept", "default",)


class CXXCtorInitializer(Node):
    attrs = ("name",)


class CXXDestructorDecl(Node):
    attrs = ("name", "virtual", "default", "noexcept",)


class AccessSpecDecl(Node):
    attrs = ("access_spec",)


class EnumDeclaration(TypeDeclaration):
    attrs = ("implements",)

    @property
    def fields(self):
        return [decl for decl in self.body.declarations if isinstance(
          decl, FieldDecl)]

    @property
    def methods(self):
        return [decl for decl in self.body.declarations if isinstance(
          decl, MethodDeclaration)]


class InterfaceDeclaration(TypeDeclaration):
    attrs = ("type_parameters", "extends",)


class AnnotationDeclaration(TypeDeclaration):
    attrs = ()


class StaticInitializer(NonEmptyDeclaration):
    attrs = ("block",)


class InstanceInitializer(NonEmptyDeclaration):
    attrs = ("block",)

# ------------------------------------------------------------------------------


class ArrayDimension(Node):
    attrs = ("dim",)


class Modifier(Node):
    attrs = ("value",)


class Operator(Node):
    attrs = ("operator",)

# ------------------------------------------------------------------------------


class Type(Node):
    attrs = ("name", "dimensions",)

class BuiltinType(Node):
    attrs = ("name",)

class ConstantArrayType(Node):
    attrs = ("type", "size", )

class FunctionProtoType(Node):
    attrs = ()

class ParenType(Node):
    attrs = ("type",)

class PointerType(Node):
    attrs = ("type",)

class QualType(Node):
    attrs = ("qualifiers",)

class DiamondType(Type):
    attrs = ("sub_type",)


class ReferenceType(Type):
    attrs = ("arguments", "sub_type",)


class TypeArgument(Node):
    attrs = ("type", "pattern_type",)

# ------------------------------------------------------------------------------


class TypeParameter(Node):
    attrs = ("name", "extends",)

# ------------------------------------------------------------------------------


class Annotation(Node):
    attrs = ("name", "element",)


class NormalAnnotation(Annotation):
    attrs = ()


class MarkerAnnotation(Annotation):
    attrs = ()


class SingleElementAnnotation(Annotation):
    attrs = ()


class ElementValuePair(Node):
    attrs = ("name", "value",)


class ElementArrayValue(Node):
    attrs = ("values",)


class InitListExpr(Node):
    attrs = ()

# ------------------------------------------------------------------------------


class Member(NonEmptyDeclaration):
    attrs = ()


class CXXMethodDecl(Declaration):
    attrs = ("virtual", "return_type", "name", "noexcept", "const", "default",)


class FunctionDecl(Declaration):
    attrs = ("return_type", "name", "variadic",)


class ClassTemplateDecl(Declaration):
    attrs = ()


class FunctionTemplateDecl(Declaration):
    attrs = ()


class TemplateTypeParmDecl(Declaration):
    attrs = ("name",)


class NonTypeTemplateParmDecl(Declaration):
    attrs = ("name", "type")


class ParmVarDecl(Node):
    attrs = ("type", "name", "dimensions",)


class ParmVarDecl(Node):
    attrs = ("type", "name", "dimensions",)


class FieldDecl(Node):
    attrs = ("type", "name", "init",)


# ------------------------------------------------------------------------------


class ConstantDeclaration(FieldDecl):
    attrs = ()


class VariableInitializer(Node):
    """
    A VariableInitializer is either an expression or an array initializer
    https://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.3
    TODO This is not C++ !!!
    """
    attrs = ("expression", "array",)


class ArrayInitializer(Node):
    attrs = ("initializers", "comma",)


class VariableDeclaration(NonEmptyDeclaration):
    attrs = ("type", "declarators",)


class LocalVariableDeclaration(VariableDeclaration):
    attrs = ()


class VariableDeclarator(Node):
    attrs = ("name", "dimensions", "initializer")


class FormalParameter(NonEmptyDeclaration):
    attrs = ("type", "name", "dimensions", "varargs")


class InferredFormalParameter(Node):
    attrs = ('expression',)

# ------------------------------------------------------------------------------


class Statement(Node):
    attrs = ("label",)


class DoStmt(Statement):
    attrs = ("cond", "body",)


class LocalVariableDeclarationStmt(Statement):
    attrs = ("variable",)


class TypeDeclarationStmt(Statement):
    attrs = ("declaration",)


class IfStmt(Statement):
    attrs = ("cond", "true_body", "false_body")


class ForStmt(Statement):
    attrs = ("init", "cond", "inc", "body")


class WhileStmt(Statement):
    attrs = ("cond", "body",)


class ContinueStmt(Statement):
    attrs = ()


class AssertStmt(Statement):
    attrs = ("condition", "value")


class LabelStmt(Statement):
    attrs = ("name", "stmt",)


class GotoStmt(Statement):
    attrs = ("target",)


class ContinueStmt(Statement):
    attrs = ("goto",)


class ThrowStmt(Statement):
    attrs = ("expression",)


class SynchronizedStmt(Statement):
    attrs = ("lock", "block")


class TryStmt(Statement):
    attrs = ("resources", "block", "catches", "finally_block")


class SwitchStmt(Statement):
    attrs = ("cond", "body",)


class BreakStmt(Statement):
    attrs = ()


class DefaultStmt(Statement):
    attrs = ("stmt",)


class BlockStmt(Statement):
    attrs = ("statements",)


# statemenents are the subnodes (from Node)
class CompoundStmt(Statement):
    attrs = ()


class ReturnStmt(Statement):
    attrs = ("value",)


class DeclRefExpr(Node):
    attrs = ("name", "kind",)


class NamespaceDecl(Node):
    attrs = ("name",)
#class Namespace(Node):
    #attrs = ("name",)


class UsingDirectiveDecl(Node):
    attrs = ("name",)


class DeclStmt(Node):
    attrs = ()


class VarDecl(Node):
    attrs = ("name", "type", "array", "storage_class", "init", "implicit", "referenced")


class TypedefDecl(Node):
    attrs = ("name", "type")


class TypeRef(Node):
    attrs = ("name",)


#class NamespaceRef(Node):
    #attrs = ("name",)


class ExpressionStmt(Statement):
    attrs = ("expression",)


class ExprWithCleanups(Node):
    attrs = ()


class CXXForRangeStmt(Node):
    attrs = ()


# ------------------------------------------------------------------------------


class TryResource(NonEmptyDeclaration):
    attrs = ("type", "name", "value")


class CatchClause(Statement):
    attrs = ("parameter", "block")


class CatchClauseParameter(NonEmptyDeclaration):
    attrs = ("types", "name")

# ------------------------------------------------------------------------------


class CaseStmt(Statement):
    attrs = ("pattern", "stmt",)


class ForControl(Node):
    attrs = ("init", "condition", "update")


class EnhancedForControl(Node):
    attrs = ("var", "iterable")


class ExprStmt(Node):
    attrs = ("expr",)

# ------------------------------------------------------------------------------


class Expression(Node):
    attrs = ()


class ElementValueArrayInitializer(Expression):
    attrs = ("initializer",)


class ReferenceTypeExpression(Expression):
    attrs = ("type",)


class BlockExpression(Expression):
    attrs = ("block",)


class NoExpression(Expression):
    attrs = ()


class Primary(Expression):
    attrs = ()
    #attrs = ("prefix_operators", "postfix_operators", "qualifier", "selectors")


class ParenExpr(Primary):
    attrs = ("expr",)


class Assignment(Primary):
    attrs = ("expressionl", "value", "type")


class BinaryOperator(Expression):
    attrs = ("opcode", "left", "right",)


class UnaryOperator(Expression):
    attrs = ("opcode", "expr", "postfix",)


class ConditionalOperator(Expression):
    attrs = ("cond", "true_expr", "false_expr")


class ArraySubscriptExpr(Expression):
    attrs = ("base", "index",)


class MethodReference(Primary):
    attrs = ("expression", "method", "type_arguments")


class LambdaExpression(Primary):
    attrs = ('parameter', 'parameters', 'body')


class CXXConstructExpr(Expression):
    attrs = ("type",)


class MaterializeTemporaryExpr(Expression):
    attrs = ()


class CXXBindTemporaryExpr(Expression):
    attrs = ()


class CXXNewExpr(Expression):
    attrs = ()


class UnaryExprOrTypeTraitExpr(Expression):
    attrs = ("name", "expr", "type")


class ImplicitCastExpr(Expression):
    attrs = ("type", "expr",)

# ------------------------------------------------------------------------------


class Identifier(Primary):
    attrs = ("id",)


class Literal(Primary):
    attrs = ("value",)


class CharacterLiteral(Literal):
    attrs = ()


class IntegerLiteral(Literal):
    attrs = ("type",)


class FloatingLiteral(Literal):
    attrs = ("type",)


class StringLiteral(Literal):
    attrs = ()


class CXXNullPtrLiteralExpr(Literal):
    attrs = ()


class CXXThisExpr(Primary):
    attrs = ()


class MemberExpr(Primary):
    attrs = ("name", "op", "expr")


class ConstantExpr(Primary):
    attrs = ("value", "expr",)


class CXXMemberCallExpr(Primary):
    attrs = ()


class CallExpr(Primary):
    attrs = ()


class CXXOperatorCallExpr(Primary):
    attrs = ("left", "op", "right",)


class CXXBoolLiteralExpr(Primary):
    attrs = ("value",)


class CXXTemporaryObjectExpr(Node):
    attrs = ("type",)


class CXXFunctionalCastExpr(Node):
    attrs = ("type",)


class NullStmt(Statement):
    attrs = ()


class Cast(Primary):
    attrs = ("type", "expression")


class FieldReference(Primary):
    attrs = ("field",)


class MemberReference(Primary):
    attrs = ("member",)


class Invocation(Primary):
    attrs = ("type_arguments", "arguments")


class ExplicitConstructorInvocation(Invocation):
    attrs = ()


class SuperConstructorInvocation(Invocation):
    attrs = ()


class MethodInvocation(Invocation):
    attrs = ("member",)


class SuperMethodInvocation(Invocation):
    attrs = ("member",)


class SuperMemberReference(Primary):
    attrs = ("member",)


class ArraySelector(Expression):
    attrs = ("index",)


class ClassReference(Primary):
    attrs = ("type",)


class VoidClassReference(ClassReference):
    attrs = ()

# ------------------------------------------------------------------------------


class Creator(Primary):
    attrs = ("type",)


class ArrayCreator(Creator):
    attrs = ("dimensions", "initializer")


class ClassCreator(Creator):
    attrs = ("constructor_type_arguments", "arguments", "body")


class InnerClassCreator(Creator):
    attrs = ("constructor_type_arguments", "arguments", "body")


class ClassBody(Node):
    attrs = ("declarations",)


class EmptyClassBody(Node):
    attrs = ()


class ImplicitValueInitExpr(Node):
    attrs = ()


class CXXConversionDecl(Node):
    attrs = ("name",)

# ------------------------------------------------------------------------------


class EnumConstantDecl(Node):
    attrs = ("name", "init",)


class EnumDecl(Node):
    attrs = ("name",)


class AnnotationMethod(NonEmptyDeclaration):
    attrs = ("name", "return_type", "dimensions", "default")


class EmptyDecl(Node):
    attrs = ()


class CStyleCastExpr(Node):
    attrs = ("type", "expr",)


class FriendDecl(Node):
    attrs = ("type",)


class CXXStdInitializerListExpr(Node):
    attrs = ()

